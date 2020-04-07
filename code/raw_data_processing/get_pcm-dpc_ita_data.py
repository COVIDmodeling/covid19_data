import pandas as pd
import numpy as np
import requests
import git

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/ita/covid/"

urls = {
        "state" : "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv",
        "county" : "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv",
}

# translate regional file
df_state = pd.read_csv(urls['state'])
df_state.columns = [
        "date", "iso_a3", "regional_code", "region", "latitude", "longitude",
        "hospitalized_with_symptoms", "intensive_care", "total_hospitalized",
        "home_isolation", "total_positive", "new_total_positive",
        "new_case", "discharged_healed", "death", "case", "test", "note_it", 
        "note_en"
]
# Add columns
df_state = df_state.assign(
        country="Italy",
        source="pcm-dpc"
)
df_state.to_csv(
        f"{datadir}pcm-dpc_case-death-test-hospitalized_state_ita.csv",
        index=False
)

# Translate provincial file
df_county = pd.read_csv(urls["county"])
df_county.columns = [
        "date", "iso_a3", "regional_code", "region", "province_code",
        "province", "province_iso_a2", "latitude", "longitude", "case",
        "note_it", "note_en"
]
# Add columns
df_county = df_county.assign(
        country="Italy",
        source="pcm-dpc"
)
df_county.to_csv(f"{datadir}pcm-dpc_case_county_ita.csv", index=False)
