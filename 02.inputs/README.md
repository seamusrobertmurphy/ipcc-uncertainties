# Input data

Every third-party dataset the manuscript reads is listed here with its publisher, the link it was retrieved from, its licence and the date it was retrieved. The same name and link sit in a comment directly above the manuscript line that reads the file, so the next reader can fetch it without opening this page.

Raw downloads stay out of git under `02.inputs/<source>/raw/`, and the manuscript fetches each one inside a guarded chunk that downloads only when the file is missing. Derived tables the manuscript writes go to `03.outputs/TBL/` and are committed.

No dataset has been retrieved yet.

## Sources

Each source takes one entry in this form.

| Field | Entry |
|---|---|
| Dataset | Full name as the publisher gives it |
| Publisher | Agency or data centre |
| Link | Landing page, and the DOI as an https link where one exists |
| Licence | Licence name |
| Retrieved | ISO date |
| Local path | `02.inputs/<source>/raw/<file>` |
| Read by | Manuscript chunk label |

### Canada land use tables

| Field | Entry |
|---|---|
| Dataset | Table 6-1, Net Greenhouse Gas Flux Estimates in the Land Use, Land-Use Change and Forestry Sector, All Inventory Years, by province and territory, National Inventory Report 1990–2024 |
| Publisher | Environment and Climate Change Canada |
| Link | https://data-donnees.az.ec.gc.ca/data/substances/monitor/canada-s-official-greenhouse-gas-inventory/E-LULUCF/?lang=en |
| Licence | Open Government Licence, Canada |
| Retrieved | 2026-10-21 |
| Local path | `02.inputs/eccc/raw/table-6-1.xlsx` |
| Read by | `analysis` |
