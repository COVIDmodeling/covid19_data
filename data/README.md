# `data`

Here we provide data, collected from a number of sources, to be used for
modeling the COVID-19 pandemic, as well as data from previous epidemics, and
data from specific published models.

## Folder Structure

Top level directories exist for each country that we have identified
datasources for. These are labeled by [ISO 3166-1 alpha3 three letter
convention](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) **in lower
case**. Additional folders exist for `global` data which contains generally
lower resolution data from many countries simultaneously, and for `published`
data that was used as the basis of published models. 

Within these top-level directories, we maintain `covid`-specific data as well
as a smattering of data relating to other diseases (e.g. `flu`), `demographics`
and other useful information.

## File naming
Where applicable, data is presented as files adhering to the custom of
`source_information_resolution_location.format`

### `source`
This indicates briefly where the data was collected from. These sources are
described in detail in the READMEs of folders where they appear. The list of
sources so far are

| Source                                                                       | Abbreviation    | URL                                                  |
| :--------------------------------------------------------------------------- | :-------------- | :--------------------------------------------------- |
| New York Times                                                               | `nyt`           | `https://github.com/nytimes/covid-19-data`           |
| Johns Hopkins University CSSE                                                | `jhu`           | `https://github.com/CSSEGISandData/COVID-19`         |
| Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile | `pcm-dpc`       | `https://github.com/pcm-dpc/COVID-19`                |
| Kaggle                                                                       | `kaggle`        | `https://www.kaggle.com/kimjihoo/coronavirusdataset` |
| USA Facts                                                                    | `usafacts`      | `https://usafacts.org/issues/coronavirus/`           |
| The COVID Tracking Project                                                   | `covidtracking` | `https://covidtracking.com`                          |
| Corona Data Scraper                                                          | `coronascraper` | `https://coronadatascraper.com/#home`                |

### `information`
This indicates briefly what information is contained on each file. Presented as
**one word in singular** to describe each aspect of data contained. If multiple
sources of information are contained in the data **separate them with a
hyphen** rather than an underscore. E.g.:
- `case` : Confirmed COVID-19 cases only.
- `death` : Confirmed COVID-19 related deaths only.
- `test` : Information about COVID-19 testing only
- `case-death` : Confirmed cases and number of deaths in single file
- `case-death-recovered`: Confirmed cases, deaths, and recovered cases.

### `resolution`
This refers to the resolution of the data available in the file. The common
entries here are:
- `country` : Where the data reported are given at a country level.
- `state` : Where the data reported are given at the state level.
- `region` : For countries that use this terminology instead of state.
- `county` : Where the data reported are given at the county level.
- `city` : Where the data reported are given at the city level

### `location`
The location that encompasses the entirety of the data recorded within a file.
If the data comes from a particular country we use the [ISO 3166-1 alpha3 three
letter convention](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) **in lower
case**. Global data is indicated with `global`.

## Data Structure
The data is stored in the long-table format also known as [`tidy
data`](http://www.jstatsoft.org/v59/i10/). This implies that each row
represents an entry for a single location at a single point in time.

## Standardized column names
The most common entires on the datasets have standardized column names. Not all
data sources list all of these columns, but when available, these names are:
- `date` : Date for the entry.
- `case` : Number of confirmed COVID-19 **cumulative** cases.
- `death` : Number of confirmed COVID-19 related **cumulative** deaths.
- `test` : Number of total tests performed.
- `recovered` : Number of confirmed COVID-19 **cumulative** cases that
  recovered.
- `source` : Source for the data. See [section on source](#source)
- `country` : Where the data reported are given at a country level.
- `iso_a3` : [ISO 3166-1 alpha3 three
  letter convention](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) name for
  the country.
- `state` : Where the data reported are given at the state level.
- `region` : For countries that use this terminology instead of state. NOTE: If
  the dataset contains regions data from countries with states and regions,
  `state` is chosen as the default column name.
- `county` : Where the data reported are given at the county level.
- `city` : Where the data reported are given at the city level
- `longitude` : Longitude of the location where the data was collected
- `latitude` : Latitude of the location where the data was collected