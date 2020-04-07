# COVID-19 data repository

As the flow of data related to the COVID-19 pandemic explodes, many times it is
difficult to maintain a standardized data format across different sources. To
avoid this we decided that compiling the data under a unique unifying format
would be necessary for our own workflow with the data. In this public
repository we compile COVID-19 related data from different following our own
self-defined internal standard.

# Repository structure
This repository follows a very simple structure:
```
covid19_data
+---code
    +---annotation
+---data
    +---{usa, ita, kor} (data for a specific country)
    +---global
    +---published (data related to a specific scientific publication)
```

## `code`
This folder contains all of the scripts used to manipulate directly the raw
data collected from different sources. Each of the `.py` files processes the
files from other people's collections and transforms it into our standardized
format. The `daily_refresh.sh` compiles all such scripts and automatically
updates all datasets every day.

### `annotation`
This folder contains auxiliary files helping to standardize the data. For
example here we have files that map from country names to [ISO 3166-1 alpha3
three letter convention](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3), or
USA state names into their [ISO
3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) format.


## `data`
We keep all of the collected data in this folder. Top level directories exist
for each country that we have identified datasources for. These are labeled by
[ISO 3166-1 alpha3 three letter
convention](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) **in lower
case**. Additional folders exist for `global` data which contains generally
lower resolution data from many countries simultaneously, and for `published`
data that was used as the basis of published models. 

Within these top-level directories, we maintain `covid`-specific data as well
as a smattering of data relating to other diseases (e.g. `flu`), `demographics`
and other useful information.

For the file-naming convention and data standardization please look at the
`data/README.md` file.