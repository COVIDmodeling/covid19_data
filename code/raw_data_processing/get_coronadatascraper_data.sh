#!/bin/bash
cd "$(git rev-parse --show-toplevel)"
wget https://coronadatascraper.com/timeseries.csv -O data/global/covid/cds_case-death-recovered-test_state_global.csv
