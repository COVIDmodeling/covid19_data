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
def clean_df(df, val_name="Cases"):
    """Cleans up dataframe"""
    # convert to longform
    if val_name == "case":
        col_idx = 11
    elif val_name == "death":
        col_idx = 12
    df = df.melt(
        value_vars=df.columns[col_idx:],
        id_vars=df.columns[0:col_idx],
        var_name="date",
        value_name=val_name
    )

    # clean datatypes
    df['Province_State'] = df['Province_State'].astype('string')
    df['Country_Region'] = df['Country_Region'].astype('string')
    df['date'] = df['date'].astype('datetime64')
    df = df.drop(columns=['Combined_Key'])

    return df

#%%
# Pull data and clean

# urls for data in Johns Hopkins github repository
urls = {"case" : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv",
        "death" : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv",
}

# Initialize dictionary to save output dataframes
output_dfs = {}

# Loop urls
for condition, url in urls.items():
    # Obtain data
    request = requests.get(url)
    # Convert into string
    txt = StringIO(request.text)
    # Convert into dataframe
    df = pd.read_csv(txt)
    # Add to dictionary
    output_dfs[condition] = clean_df(df, val_name=condition)

# Merge dataframes into single one
df = (output_dfs['case']
      .merge(output_dfs['death'])
    )

# Rename columns
df = df.rename(
    columns={"Country_Region": "country",
             "Province_State": "state",
             "iso2": "iso_a2",
             "iso3": "iso_a3",
             "Lat": "latitutde",
             "Long_": "longitude",
             "Population": "population",
             "Admin2": "county"
             }
)

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
resourcedir = f"{homedir}/code/annotation/"
datadir = f"{homedir}/data/usa/covid/"

# Add iso_a3 abreviation for country and source
df= df.assign(
    source="jhu"
)
# Turn all columns to lowercase
df.columns = map(str.lower, df.columns)

# Store new tidy data-frames
df.to_csv(
    f"{datadir}jhu_case-death_county_usa.csv",
    index=False
)
