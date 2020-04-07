## Global COVID-19 Data

These data are acquired from the following sources:
- `jhu`: [Johns Hopkins University CSSE github repo](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
- `cds`: [Corona Data Scraper](https://coronadatascraper.com/timeseries.csv), which aggregates data from governments and health departments around the globe
- `ecdc`: European Center for Disease Control and Prevention, as aggregated by [Our World in Data](https://ourworldindata.org/coronavirus)

Data in these sheets are presented as:
- **`county`**: Where provided (mostly the US), the highest geographical resolution.
- **`state`**: Non-abbreviated province or state listing, where provided.
- **country**: Data source-provided country name.
- **`lat`**: JHU provided latitude of geographic center of region.
- **`long`**: JHU provided longitude of geographic center of region.
- **`date`**: Date of observation, as YYYY-MM-DD.
- **`case`**: No. of cumulative confirmed cases for the region on date of observation.
- **`death`**: No. of cumulative deaths for the region on date of observation.
- **iso_a3** : [ISO 3166-1 alpha 3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) three letter code of the country.
