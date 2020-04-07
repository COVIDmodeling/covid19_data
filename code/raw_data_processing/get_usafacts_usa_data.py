#%%
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
from io import StringIO
import os
import us
import git

#%%
# List urls
urls = {
    "case": "https://static.usafacts.org/public/data/covid-19/covid_confirmed_usafacts.csv",
    "death": "https://static.usafacts.org/public/data/covid-19/covid_deaths_usafacts.csv"
}

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/usa/covid/"
resourcedir = f"{homedir}/code/processing/raw_data_processing/annotation/"
# %%
# Read states general information
df_states = pd.read_csv(f"{resourcedir}usa_states_code.csv")

# Initialize dictionary to save dataframes
df_dict = {}

# Loop through urls
for key, url in urls.items():
    # Read confirmed cases data
    request = requests.get(urls[key])
    # Convert into string
    txt = StringIO(request.text)
    # Convert into dataframe
    df = pd.read_csv(txt)

    # Melt into long format
    df = df.melt(
        value_vars=df.columns[4:],
        id_vars=df.columns[0:4],
        var_name="date",
        value_name=key
    )
    # rename columns
    df = df.rename(columns={
        "countyFIPS": "county_fips",
        "stateFIPS": "state_fips",
        "County Name": "county",
        "State": "state_iso_a2",
        })
    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])
    # save dataframes
    df_dict[key] = df
#%%
# Merge dataframes 
df = pd.merge(df_dict["case"], df_dict["death"], how="outer")
# List columns
col = list(df.columns)
# Find the weird one with uppercaes (hard to remove)
col_rm = [c for c in col if c[-1].isupper()]
# drop column that gave this result
df = df.drop(columns=col_rm)

# Generate name dictionary
name = dict(zip(df_states["state"], df_states["name"]))
longitude = dict(zip(df_states["state"], df_states["longitude"]))
latitude = dict(zip(df_states["state"], df_states["latitude"]))
# Add extra columns
df = df.assign(
    state=[name[x] for x in df["state_iso_a2"]],
    longitude=[longitude[x] for x in df["state_iso_a2"]],
    latitude=[latitude[x] for x in df["state_iso_a2"]],
    iso_a3="USA",
    source="usafacts"
)
# Save dataframe
df.to_csv(f"{datadir}usafacts_case-death_county_usa.csv", index=False)
# %%