# Charting rule

Written 25 October 2026 for the scoping review of `ipcc-uncertainties`. It is the
instruction given to the language model that charted every included and undecided work
from its title and abstract, so that the Introduction and the Discussion could cite what
each work reported against the review's questions.

The manuscript asks what separating natural from human-caused disturbance, as the IPCC
2019 Refinement allows, does to the emissions Canada and British Columbia report, to their
uncertainty and to the credit a jurisdiction could earn under a crediting standard; where
that separation is hard to apply; and whether the FAOSTAT fire emissions can be reproduced
from the method FAOSTAT publishes.

The review's five questions are these.

1. `q1`. The effect of separating natural disturbance, or of the managed land proxy, on the
   land sector emissions a country or region reports, their trend and their uncertainty.
2. `q2`. Record lengths, baselines, thresholds and statistical models used to describe a
   fire or disturbance regime, to define its natural range of variation, or to mark a year
   as exceptional.
3. `q3`. How the uncertainty of forest and land carbon flux estimates has been quantified,
   and how disturbance and year-to-year variation are treated within it.
4. `q4`. Global or national fire emission datasets and methods, such as FAOSTAT, GFED, GFAS,
   IPCC Tier 1 defaults, the fire module of a carbon budget model or the Fire and Fuels
   Extension of the Forest Vegetation Simulator, their reproduction, and their comparison
   with what countries report.
5. `q5`. A forest carbon account run with and without a separation of natural disturbance,
   or the credit, buffer, reversal or permanence of forest carbon under a crediting
   standard or a jurisdictional programme.

## Fields

Write one CSV line per record with the header
`row,questions,place,scale,method,disturbance,finding,quote,basis,role`, every field in
double quotes, in the file's order.

1. `row` is the record's code, such as `r0123`.
2. `questions` lists every question the record bears on, separated by spaces, such as
   `q1 q3`. Write `none` when it bears on none of them.
3. `place` is the country, province, state or region the record studied, such as
   `Canada`, `British Columbia`, `EU`, `Australia`, `boreal`, or `global`. Write
   `unspecified` when the title and abstract name none.
4. `scale` is one of `stand`, `landscape`, `regional`, `national`, `global` or `none`.
5. `method` is the one main method or model, chosen from this list. `CBM-CFS3`,
   `other carbon budget model`, `process or vegetation model`, `FVS or FFE`,
   `IPCC default factors`, `FAOSTAT`, `global fire emissions dataset`,
   `national forest inventory`, `remote sensing`, `flux measurement`,
   `fire history reconstruction`, `statistical model of a regime`,
   `uncertainty analysis`, `accounting rules or policy`, `review`, `other`.
6. `disturbance` is one of `fire`, `insects`, `harvest`, `storm`, `drought`,
   `land-use change`, `several` or `none`.
7. `finding` is at most 35 words, in plain words and the past tense, saying what the record
   found or did, with its number where the abstract gives one. Report only what the
   abstract or title states. Never add a finding from memory of the paper.
8. `quote` is one passage of at most 30 words copied exactly from the abstract, character
   for character, that supports the finding. It will be checked mechanically against the
   abstract, so do not change spelling, spacing, punctuation or capitals, and do not join
   two passages. Leave it empty when there is no abstract.
9. `basis` is `abstract` when an abstract was given, otherwise `title`.
10. `role` is `central` when the record is directly about separating natural from human
    effects in reported emissions, removals or credit, a record length or threshold used to
    class disturbance as natural, the uncertainty of a national or jurisdictional forest
    carbon estimate, the comparison of fire emission estimates with what countries report,
    or the buffer or reversal risk of forest carbon credits. Otherwise it is `context`.

Records with no abstract are charted from the title, venue and year alone, with
`basis` set to `title`, an empty `quote`, and a `finding` that says only what the title
states.

Check before finishing that the CSV has exactly one line per record in your file and that
every `quote` appears word for word in that record's abstract.
