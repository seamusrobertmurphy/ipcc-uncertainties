# Screening rule

The records come from a scoping review behind a manuscript on separating natural from
human-caused disturbance in the land sector greenhouse gas reporting of a country. Canada
and British Columbia are the case, and the subject is the natural disturbance provision of
the IPCC 2019 Refinement, its effect on reported emissions and their uncertainty, and the
credit a jurisdiction could earn under a crediting standard.

The author screened the first records himself and described his rule in these words.

> "I basically looked for any mention of anthropogenic disturbances or any mention of
> disturbances separated from natural disturbances, or in fact, any mention of
> anthropogenic disturbances or natural disturbances or human-induced disturbances or any
> such kind of disturbances in the title or the abstract, and then that determined whether
> it was to be included."

His decisions show that he applied this rule inside the review's five questions, not as a
bare word match. A record that mentions disturbance but has nothing to do with the
questions was excluded, and a record on separating natural from human effects in carbon
accounting was included even when the word disturbance does not appear.

1. Q1. The effect of separating natural disturbance, or of the managed land proxy, on the
   land sector emissions a country or region reports, their trend and their uncertainty.
2. Q2. Record lengths, baselines, thresholds and statistical models used to describe a
   fire or disturbance regime, to define its natural range of variation, or to mark a year
   as exceptional.
3. Q3. How the uncertainty of forest and land carbon flux estimates has been quantified,
   and how disturbance and year-to-year variation are treated within it.
4. Q4. Global fire emission datasets such as FAOSTAT, GFED or GFAS, their reproduction,
   and their comparison with what countries report.
5. Q5. A country's or jurisdiction's forest carbon account run with and without a
   separation of natural disturbance, comparing emissions, uncertainty or credit.

## Include

The test has two parts, and a record is included only when it passes both.

First, disturbance, natural or human-caused, or the separation of natural from human
effects, is a central subject of the record. It is named in the title, or it carries the
main method or the main finding of the abstract. A record in which disturbance appears only
in passing, as one background driver among several, or as context for a study whose
subject is something else, fails this part.

Second, the record does at least one of these.

1. Treats disturbance, natural (fire, insects, disease, wind, storms, drought) or
   human-caused (harvest, land use change, deforestation, degradation), as a cause of
   change in forest or land carbon stocks, emissions, removals or sinks, and estimates,
   models, attributes, separates, accounts for or reports that change at a landscape,
   regional, national or global scale. Inventories, carbon budget models such as CBM-CFS3,
   accounting rules, reference levels and national reporting all count.
2. Concerns how natural, indirect or human effects are separated, factored out or excluded
   in carbon accounting or reporting, such as factoring out, the managed land proxy, the
   natural disturbance provision, Kyoto Protocol land use accounting, forest reference
   levels, or natural against anthropogenic sinks, even when the word disturbance does not
   appear. National forest carbon monitoring, accounting and reporting systems also count.
3. Reports the statistics of a disturbance regime, such as a fire cycle, fire return
   interval, time since fire, an age-class distribution read as a fire history, negative
   exponential or Weibull models, the historical or natural range of variability, the
   record length or baseline period, or a threshold for an extreme or exceptional year.
4. Treats disturbance or the variation from year to year as part of the uncertainty or
   variability of a forest or land carbon flux estimate.
5. Estimates fire emissions from global or national datasets, compares them with national
   inventories, or tries to reproduce them.

## What the author's decisions show

A first version of this rule, which told the screener to include generously, agreed with
the author on 38 of his 53 records, and nearly every disagreement was a record the author
excluded and the screener included. Read the worked examples in the examples file before
screening. The pattern they show, as read by the person who wrote this rule, is this.

1. A paper about how to manage forests for carbon, about forestry practice or an industry,
   or about policy, was excluded when disturbance was only part of its background, and
   included when natural disturbance or its risk was the subject, as a title that names it
   shows.
2. A product that maps or catalogues disturbance, such as a database of storm damage or a
   map of defoliation from satellite images, was excluded even when it was compared with
   inventory data, unless it estimated carbon.
3. A study of carbon in cropland soils was excluded.
4. Papers on national forest carbon accounting systems, carbon budget models, reference
   levels and the rules for separating natural from human effects were included, as were
   the papers on how natural disturbance enters an inventory.
5. A copy of a work in another language was excluded.

When unsure, look at the title. Include when the title names a disturbance, a disturbance
agent such as fire or insects, the separation of natural from human effects, or national
forest carbon reporting or accounting. Otherwise exclude.

## Exclude

Give one code with every exclusion.

1. `off-topic`. The word means something else in another field, such as disturbance in
   physics, medicine, psychology or engineering, fire in buildings, or inventory in retail.
2. `wrong-population`. The right concept in a system the review does not cover, such as
   coral reefs, lakes, the ocean, cities or a laboratory.
3. `wrong-concept`. Forest or land, but none of the concepts above. Typical cases are the
   detection or mapping of disturbance from imagery with no carbon estimate and no regime
   statistics, plot or stand ecology with no estimate at landscape scale or larger and no
   link to accounting, and management, policy or carbon market papers that do not treat
   disturbance or the separation of natural from human effects.
4. `not-research`. An editorial, news item or data record with nothing on the topic. A
   correction notice or reply to referees whose subject is on topic is decided on that
   subject.
5. `not-english`. The full text is not in English. A title or abstract given only in
   another language means not English. A title given in two languages, one of them
   English, is decided on its subject.

Do not use `duplicate`. Decide every copy of a work on its own merits.

## Mismatched abstracts

Some abstracts came from the wrong record in the index. When an abstract plainly describes
a different work from its title, decide on the title alone and say so in the note.

## Records with no abstract

Judge from the title, venue and year. Include when the title plainly falls under one of the
five include cases. When the title could go either way and there is no abstract, write
`undecided`.

## Output

Write a CSV with the header `row,decision,reason,note` and one line for every record in
your file, in the file's order, every field in double quotes.

1. `row` is the record's code, such as `r0123`.
2. `decision` is `include`, `exclude` or `undecided`.
3. `reason` is the code for an exclusion, and for every other decision the code that would
   apply if it were excluded, so that the field is never empty.
4. `note` is at most 15 words naming what the record is about and why it was decided so.

Check before finishing that the CSV has exactly one line per record in your file.
