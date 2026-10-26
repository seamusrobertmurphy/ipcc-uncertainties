#!/usr/bin/env python3
"""Stop the render when the manuscript depends on code it does not contain.

The hard rule of this repository is that only code inside 01.manuscript/Manuscript.qmd
counts, and every number the paper reports comes from R running that file. This guard
reads the manuscript and fails on each way the rule has been broken before:

  1. a chunk hides its code with echo: false, include: false or code-fold,
  2. a chunk is switched off with eval: false,
  3. a chunk calls code kept in another file, through source(), sys.source(),
     knitr::read_chunk(), reticulate::source_python(), a Quarto include or a
     child document,
  4. a chunk shells out to Rscript, python or bash, through system() or system2(),
  5. a chunk reads anything under 05.tasks/, which holds correspondence only,
  6. a chunk in an engine other than R.

Run:  python3 01.manuscript/_tools/check-manuscript-code.py [file.qmd]
Exits 1 and names every offending chunk. Wired into _quarto.yml as a pre-render step.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
QMD = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01.manuscript" / "Manuscript.qmd"

CHUNK = re.compile(r"^```\{(\w+)[^}]*\}\s*\n(.*?)^```", re.S | re.M)
OPTION_RULES = [
    (r"#\|\s*echo:\s*false", "hides its code with echo: false"),
    (r"#\|\s*include:\s*false", "hides its code with include: false"),
    (r"#\|\s*code-fold:\s*true", "folds its code away"),
    (r"#\|\s*eval:\s*false", "is switched off with eval: false"),
]
CODE_RULES = [
    (r"\b(?:sys\.)?source\s*\(", "runs code from another file with source()"),
    (r"read_chunk\s*\(", "reads chunks from another file"),
    (r"source_python\s*\(", "runs a Python file"),
    (r"\bsystem2?\s*\(", "shells out with system() or system2()"),
    (r"05\.tasks", "reads from 05.tasks/"),
]

text = QMD.read_text(encoding="utf8")
problems = []

for m in re.finditer(r"\{\{<\s*include\s+([^>]+)>\}\}", text):
    problems.append(f"include directive pulls in {m.group(1).strip()}")

chunks = list(CHUNK.finditer(text))
for m in chunks:
    engine, body = m.group(1), m.group(2)
    line = text.count("\n", 0, m.start()) + 1
    label = re.search(r"#\|\s*label:\s*(\S+)", body)
    name = f"{label.group(1) if label else 'unlabelled chunk'} (line {line})"
    if engine != "r":
        problems.append(f"{name} is a {engine} chunk; only R chunks are run by the manuscript")
    if re.search(r"#\|\s*child:", body):
        problems.append(f"{name} pulls in a child document")
    options = "\n".join(l for l in body.splitlines() if l.lstrip().startswith("#|"))
    code = "\n".join(l.split("#", 1)[0] for l in body.splitlines() if not l.lstrip().startswith("#"))
    problems += [f"{name} {why}" for rx, why in OPTION_RULES if re.search(rx, options)]
    problems += [f"{name} {why}" for rx, why in CODE_RULES if re.search(rx, code)]

header = text.split("---", 2)[1] if text.startswith("---") else ""
if re.search(r"^\s*echo:\s*false", header, re.M):
    problems.append("the YAML header sets echo: false for every chunk")

print(f"{QMD.relative_to(ROOT) if QMD.is_relative_to(ROOT) else QMD}: {len(chunks)} chunks checked")
if problems:
    print("\nThe manuscript depends on code it does not show or does not contain:")
    for p in problems:
        print(f"  {p}")
    print("\nMove the code into a visible R chunk in the manuscript, or delete the dependency.")
    sys.exit(1)
print("every chunk is visible R code that lives in the manuscript")
