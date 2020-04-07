#%%
import pandas as pd
import requests
from io import StringIO
import os
import us
import git

#%%
# List urls
urls = {
    "state": "https://github.com/nytimes/covid-19-data/raw/master/us-states.csv",
    "county": "https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv"
}

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/usa/covid/"
resourcedir = f"{homedir}/code/processing/raw_data_processing/annotation/"
# Read states general information
df_states = pd.read_csv(f"{resourcedir}usa_states_code.csv")

# Generate name dictionary
name = dict(zip(df_states["name"], df_states["state"]))
longitude = dict(zip(df_states["name"], df_states["longitude"]))
latitude = dict(zip(df_states["name"], df_states["latitude"]))
# Add extra columns
# %%
#%% Loop through each dataset and make necessary changes
for key, url in urls.items():
    # Obtain data
    request = requests.get(url)
    # Convert into string
    txt = StringIO(request.text)
    # Convert into dataframe
    df = pd.read_csv(txt)
    # Rename columns
    df = df.rename(columns={"cases": "case", "deaths": "death"})
    # Make sure all headers are lowercase
    df.columns = map(str.lower, df.columns)
    # Add columns with more information
    df = df.assign(
        state_iso_a2=[name[x] for x in df["state"]],
        longitude=[longitude[x] for x in df["state"]],
        latitude=[latitude[x] for x in df["state"]],
        source="nyt",
        iso_a3="USA"
    )
    # Save dataframe
    df.to_csv(f"{datadir}nyt_case-death_{key}_usa.csv", index=False)
# %%
