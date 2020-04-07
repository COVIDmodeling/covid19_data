#!/bin/bash

cd "$(git rev-parse --show-toplevel)"
cd code/processing/raw_data_processing
python3 get_jhu_global_data.py
python3 get_jhu_usa_data.py
python3 get_nyt_usa_data.py
python3 get_usafacts_usa_data.py
python3 get_covidtracking_usa_data.py
python3 get_pcm-dpc_ita_data.py
python3 get_kaggle_kor_data.py
./get_coronadatascraper_data.sh
./get_ECDC_data.sh
