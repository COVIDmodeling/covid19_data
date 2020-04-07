#!/bin/bash
cd "$(git rev-parse --show-toplevel)"
wget https://covid.ourworldindata.org/data/ecdc/full_data.csv -O data/global/covid/ecdc_case-death_country_global.csv
cd code/
python3 aggregate_our_world_in_data.py
