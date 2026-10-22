# Review protocol

Written 22 October 2026 for `ipcc-uncertainties`, before any recorded query ran. Follows
`library-science/protocols/literature-review.md`, escalated to the full method of the
`scoping-review` skill because the manuscript's contribution rests on a claim that a
comparison has not been made before, and reported against PRISMA-ScR (Tricco et al. 2018).
Frozen by the commit that adds it, and nothing above "Deviations" is edited after that
commit.

The review has two depths, set by Seamus on 22 October 2026. Separating natural from
human-caused disturbance in greenhouse gas reporting is "a bleeding edge new field of
science", while "the statistics of ecology disturbance and carbon fluctuations is age old".
Questions 2 and 3 therefore reach back as far as the indexes go.

## Objectives

Copied verbatim from the Introduction of `01.manuscript/Manuscript.qmd` on 22 October 2026,
which restates the question Seamus set for the repository on that date, "disaggregating
anthropogenic from natural disturbances, as part of the new IPCC guideline, and what
difference that makes to national scale emissions reporting", together with "where are
the challenges" and the reproduction of the FAOSTAT method.

1. What difference does separating natural from human-caused disturbance, as the 2019
   Refinement allows, make to the emissions Canada and British Columbia report, to their
   uncertainty and to the credit they could claim?
2. Where does the separation become hard to apply, in the length of record behind a
   natural disturbance test, in the period over which regrowth is tracked, and in an
   uncertainty taken on a net near zero?
3. Can the fire emissions a government starts from be reproduced from the method FAOSTAT
   publishes and the IPCC Tier 1 steps it cites, and where does the published method fall
   short?

## Questions

Each question is searched by one or more routes, named `q1`, `q2a` and so on in
`search-terms.csv`, and every route of a question is screened as that question.

1. What has been found about the effect of separating natural disturbance, or of the
   managed land proxy it corrects, on the land sector emissions a country reports, their
   trend and their uncertainty? Population national and subnational land sector accounts,
   concept the natural disturbance provision and the managed land proxy, context UNFCCC
   reporting, the Kyoto Protocol and the Paris Agreement. Routes `q1` and `q1b`.
2. What record lengths, baselines, thresholds and statistical models have been used to
   describe a fire or disturbance regime, to define its natural range of variation, or to
   mark a year as exceptional? Population forests and other fire-prone land, concept the
   statistics of disturbance regimes, context ecology and fire science of any period.
   Routes `q2a`, `q2b` and `q2c`.
3. How has the uncertainty of forest and land carbon flux estimates been quantified, and
   how have disturbance and the variation from year to year been treated within it?
   Population forest and land carbon budgets, concept uncertainty and interannual
   variability of carbon flux, context carbon budget models, flux measurement and
   inventories of any period. Routes `q3` and `q3b`.
4. How far can global fire emission datasets, FAOSTAT among them, be reproduced from their
   published methods, and how do they compare with what countries report to the UNFCCC?
   Population global and national fire emission estimates, concept reproduction and
   comparison, context national greenhouse gas inventories. Route `q4`.
5. Novelty. Has any study run a country's or jurisdiction's forest carbon account with and
   without a separation of natural disturbance and compared the emissions, uncertainty or
   credit of the two? Population national and jurisdictional forest carbon accounts,
   concept the two accounts compared, context reporting and crediting. Route `q5`, and
   every record retained under question 1.

## Adjudication

1. If a study has already reported Canada's or another country's land sector emissions
   with and without the separation over the inventory period, the manuscript reports its
   own comparison as an update to the 2026 inventory and to British Columbia, and cites
   that study as the method it follows.
2. If prior work sets a minimum record length for estimating a fire regime or its range of
   variation, the statement that the guidance "sets no length" is narrowed to the IPCC
   guidance, and the 13, 20 and 30 year baselines are compared with that minimum. If prior
   work has shown that the years classed as natural do not change with baseline length,
   that result is reported as a replication.
3. If prior work has shown that a percentage uncertainty grows without bound as a net flux
   nears zero in a forest or land inventory, the manuscript claims only the application to
   crediting, not the finding. If prior work shows that the separation narrows the
   absolute uncertainty of the reported account, the Discussion answers that result.
4. If a study has already reproduced the FAOSTAT fire emissions from its published method,
   or found the same undocumented steps, the manuscript cites it and reports its own
   reproduction as confirmation, extended to organic soil fires.
5. If any study has compared the credit or the uncertainty of the two accounts, the
   manuscript is reported as an extension of it, and the abstract's "little is known" is
   rewritten.

## Criteria

1. Document types admitted are peer-reviewed articles, reviews, chapters and conference
   papers, and agency reports, IPCC guidelines, UNFCCC decisions, national inventory
   reports and crediting standards where they are the primary source of a method,
   threshold, rule or data product.
2. No opening year for any question, and records published up to the date each search
   ran, because the statistics of disturbance regimes and carbon flux predate national
   inventories by decades.
3. English only.
4. A record bears on at least one question, meaning the effect of the separation on
   reported emissions, disturbance regime statistics or baselines, carbon flux uncertainty
   or interannual variability, the reproduction of fire emission datasets, or the credit
   earned by a forest carbon account.

Exclusions use the codes in the store protocol. No code is added.

## Sources

1. `library-science`, searched with the `review-store` chunk, which matches titles and
   the text of source notes.
2. OpenAlex, searched with the `review-openalex` chunk on titles and abstracts. The
   unkeyed service allowed $0.10 of queries a day from this network on 22 October 2026,
   about 100 requests, and limited any query with more than five boolean operators, so
   the chunk pauses between pages and retries a refused request.
3. Semantic Scholar bulk search, with the `review-semantic-scholar` chunk. It refused every
   unkeyed request with HTTP 429 during piloting on 22 October 2026, so a refusal at search
   time is logged as an error in `review-search-log.csv` and reported, not hidden.
4. Grey literature sought by hand, with route `grey`, URL and retrieval date, from the
   IPCC Task Force on National Greenhouse Gas Inventories, the UNFCCC decisions on land
   use accounting and the national inventory reports of parties that separate natural
   disturbance, the crediting standards of Architecture for REDD+ Transactions, Verra and
   the Forest Carbon Partnership Facility, and the FAO notes behind FAOSTAT.
5. One round of backward and forward citation chasing from no more than five central
   records per question, chosen after screening.

Scopus and Web of Science need institutional keys and Google Scholar allows no automated
access, so none is searched, and the Methods says so.

Search terms are selected in `04.references/review/search-terms.csv`, from candidates the
`review-terms` chunk draws from the manuscript's title, subtitle and keywords, and
committed with this file. The queries are built from that selection by the
`review-queries` chunk.

## Pilot

The strings were piloted on OpenAlex on 22 October 2026 by counting matches only, so that
no question would return too few records to map or too many to read. The counts were 60
for `q1`, 308 for `q1b`, 112 for `q2a`, 96 for `q2b`, 108 for `q2c`, 142 for `q3`, 93 for
`q3b`, 66 for `q4` and 53 for `q5`. A first form of `q1`, without the Kyoto Protocol and
carbon accounting terms, returned 24 and was widened. No record from the pilot was kept.

## Screening and reading

Seamus screens every title and abstract, with no reading budget for any question, and
enters a decision and, for an exclusion, a reason code in `review-records.csv`. Abstracts
are kept beside it in `02.inputs/review/raw/review-abstracts.csv`, outside git, because
they are the publishers' text. Full texts are read under step 8 of the store protocol, and
every candidate for the novelty question is read in full, because an absence is the
review's strongest claim. No critical appraisal of study quality is made, and the Methods
says so.

## Deviations

None yet.
