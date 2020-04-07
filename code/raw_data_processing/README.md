## `processing`

Run `./daily_refresh.sh` to update COVID data from JHU and usafacts. The
scripts in this folder currently rely on the following python packages:

- numpy
- pandas
- requests
- gitpython
- us
- kaggle

All are installable from pip. For Kaggle (required for updating South Korea
data), you must have a valid authentication file at ~/.kaggle/kaggle.json


### Scripts

| Script                          | Output |
| --------------------------------| ------ |
| `get_jh_global_data.py`         | `data/international/covid/jhu_data/jhu_case-death-recovered_state_global.csv` |
| `get_jh_usa_data.py`         | `data/international/covid/jhu_data/jhu_case-death_county_usa.csv` |
| `get_nyt_usa_data.py`           | `data/us/covid/nyt_case-death_{state/county}_usa.csv` |
| `get_usafacts_usa_data.py`      | `data/us/covid/usafacts_case-death_county_usa.csv` |
| `get_covidtracking_usa_data.py` | `data/us/covid/covidtracking_test-case-hospitalized-death_state_usa.csv` |
| `get_coronadatascraper_data.sh` | `data/global/covid/cds_case-death-recovered-test_state_global.csv` |
| `get_kaggle_kor_data.py`        | `data/kor/covid/{}.cvs` |
| `get_pcm-dpc_ita_data.py`       | `data/ita/covid/pcm-dpc_case_county_ita.csv` |
| `get_us_county_covid_data.sh`   | `data/us/covid/{confirmed_cases,deaths}.csv` |
| `get_ECDC_data.sh`              | `data/international/covid/our_world_in_data/full_data.csv` |


### Common errors

1. Earliest date that can be fetched from JHU data is YESTERDAY's date, not
   today's.

2. Be sure the scripts are running Python 3. `./daily_refresh.sh` calls
   `python` on the python scripts. In cases where your `python` is binded to
   Python 2, you might need to explicitly specify `python3` and `pip3` instead
   of the respective python or pip calls in order for Python 3 to see the
   packages.

3. Need to install us and git python packages: `pip install us` and `pip
   install GitPython`.

4. Pandas error where `TypeError: data type "string" not understood` : Need to
   upgrade your version of Pandas to latest version: `pip install pandas
   --upgrade`
