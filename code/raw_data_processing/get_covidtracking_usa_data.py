#%%
import pandas as pd
import requests
from io import StringIO
import os
import us
import git
import re

#%%
url = "http://covidtracking.com/api/states/daily.csv"

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/usa/covid/"
resourcedir = f"{homedir}/code/processing/raw_data_processing/annotation/"
# Read states general information
df_states = pd.read_csv(f"{resourcedir}usa_states_code.csv")

# Generate name dictionary
name = dict(zip(df_states["state"], df_states["name"]))
longitude = dict(zip(df_states["state"], df_states["longitude"]))
latitude = dict(zip(df_states["state"], df_states["latitude"]))
#%%
# Obtain data
request = requests.get(url)
# Convert into string
txt = StringIO(request.text)
# Convert into dataframe
df = pd.read_csv(txt)
# Conver date to datetime
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
# rename columns
df = df.rename(columns={"state": "state_iso_a2"})
# %%
# Split CamelCase in all titles
def camel_to_snake(string):
    """
    Function to split CamelCase and turn into snake_case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    
#%%
# List CamelCase columns
camel_cols = df.columns
# Convert to snake_case
snake_cols = [camel_to_snake(col) for col in camel_cols]
# Rename columns
df = df.rename(columns=dict(zip(camel_cols, snake_cols)))

# %%
# Add extra information columns
df = df.assign(
        state=[name[x] for x in df["state_iso_a2"]],
        longitude=[longitude[x] for x in df["state_iso_a2"]],
        latitude=[latitude[x] for x in df["state_iso_a2"]],
        source="covidtracking",
        iso_a3="USA"
    )

# Write dataframe
df.to_csv(f"{datadir}covidtracking_test-case-hospitalized-death_state_usa.csv")