#!/usr/bin/env python3
"""Count the rendered manuscript and fill its word count placeholders.

The manuscript carries placeholders that this script replaces with the rendered
document's own counts, so a declared length cannot drift from the document:

    {{WC_PROSE}}  {{WC_TOTAL}}  {{WC_ABSTRACT}}

WC_PROSE is running text without tables, captions, code or references. WC_TOTAL adds
tables, captions and references. WC_ABSTRACT is the Abstract section alone, found by
position between its heading and the next heading, and is in neither total.

No target journal has been chosen, so no limit is compared. When one is, read its
current guide for authors, record the page, the date and the verbatim wording beside the
limit in LIMITS, and the script will report any excess on every render.

Run:  python3 01.manuscript/_tools/stamp-wordcounts.py <file.docx>
Wired into _quarto.yml as a post-render step, after format-tables.py.
"""
import os
import re
import shutil
import sys
import pathlib
import zipfile
from lxml import etree

# stem of the rendered file: (prose limit, abstract limit), each with its verified source
LIMITS = {}

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
w = lambda tag: f"{{{W}}}{tag}"
WORD = re.compile(r"[A-Za-z0-9À-ɏ][A-Za-z0-9À-ɏ'’.\-/]*")


def words(text):
    return len(WORD.findall(text))


def para_text(p):
    return "".join(n.text or "" for n in p.iter(w("t")))


def style_of(p):
    s = p.find(f"{w('pPr')}/{w('pStyle')}")
    return s.get(w("val")) if s is not None else ""


def measure(root):
    counts = dict(prose=0, captions=0, tables=0, refs=0, abstract=0)
    in_abstract = False
    for child in root.find(w("body")):
        if child.tag == w("tbl"):
            counts["tables"] += words(" ".join(n.text or "" for n in child.iter(w("t"))))
            continue
        if child.tag != w("p"):
            continue
        st, txt = style_of(child), para_text(child)
        if st.startswith("Heading"):
            in_abstract = re.sub(r"^[\d.]+\s*", "", txt.strip().lower()) == "abstract"
            counts["prose"] += 0 if in_abstract else words(txt)
        elif st in ("Title", "Subtitle", "Author", "Date", "AbstractTitle", "SourceCode"):
            continue
        elif st == "Bibliography":
            counts["refs"] += words(txt)
        elif in_abstract:
            counts["abstract"] += words(txt)
        elif "aption" in st:
            counts["captions"] += words(txt)
        else:
            counts["prose"] += words(txt)
    return {
        "WC_PROSE": counts["prose"],
        "WC_TOTAL": counts["prose"] + counts["captions"] + counts["tables"] + counts["refs"],
        "WC_ABSTRACT": counts["abstract"],
    }


def process(path):
    path = pathlib.Path(path)
    if not path.exists():
        print(f"  skipped, not found: {path}")
        return
    zin = zipfile.ZipFile(path)
    parts = {n: zin.read(n) for n in zin.namelist()}
    zin.close()
    root = etree.fromstring(parts["word/document.xml"])
    counts = measure(root)

    print(f"  {path.name}: prose {counts['WC_PROSE']:,}, total with tables, captions and "
          f"references {counts['WC_TOTAL']:,}, abstract {counts['WC_ABSTRACT']:,}")
    if path.stem in LIMITS:
        prose_max, abstract_max = LIMITS[path.stem]
        over = [f"prose over by {counts['WC_PROSE'] - prose_max:,}"] * (counts["WC_PROSE"] > prose_max)
        over += [f"abstract over by {counts['WC_ABSTRACT'] - abstract_max:,}"] * (counts["WC_ABSTRACT"] > abstract_max)
        if over:
            print(f"\n{'!' * 74}\n  OVER THE LIMIT: {'; '.join(over)}.\n{'!' * 74}\n")
    else:
        print("  no verified journal limit recorded, so no limit was compared")

    hits = 0
    for p in root.iter(w("p")):
        txt = para_text(p)
        if "{{WC_" not in txt:
            continue
        for k, v in counts.items():
            txt = txt.replace("{{" + k + "}}", f"{v:,}")
        runs = p.findall(w("r"))
        for extra in runs[1:]:
            p.remove(extra)
        for t in runs[0].findall(w("t")):
            runs[0].remove(t)
        t = etree.SubElement(runs[0], w("t"))
        t.text = txt
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        hits += 1
    if not hits:
        return
    parts["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    tmp = path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in parts.items():
            zout.writestr(name, data)
    shutil.move(tmp, path)
    print(f"  {path.name}: {hits} word count placeholder paragraph(s) filled")


if __name__ == "__main__":
    args = sys.argv[1:] or [f for f in os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").split("\n")
                            if f.strip().endswith(".docx")]
    if not args:
        print("no .docx to count")
    for a in args:
        process(a.strip())
