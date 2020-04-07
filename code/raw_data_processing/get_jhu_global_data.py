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
    df = df.melt(
        value_vars=df.columns[4:],
        id_vars=df.columns[0:4],
        var_name="Date",
        value_name=val_name
    )

    # clean datatypes
    df['Province/State'] = df['Province/State'].astype('string')
    df['Country/Region'] = df['Country/Region'].astype('string')
    for i in range(len(df['Date'])):
        row = df['Date'][i]
        if '202' in row:
            df['Date'][i] = row.replace('202', '20') # they had 3/21/202 instead of 3/21/20 in their dataset
    df['Date'] = df['Date'].astype('datetime64')

    return df

#%%
# Pull data and clean

# urls for data in Johns Hopkins github repository
urls = {'Confirmed' : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        'Deaths' : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        'Recovered' : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
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
df = (output_dfs['Confirmed']
      .merge(output_dfs['Deaths'])
    )
df = df.merge(output_dfs['Recovered'])

# Rename columns
df = df.rename(
    columns={"Date": "date",
             "Confirmed":"case",
             "Deaths": "death",
             "Recovered": "recovered",
             "Country/Region": "country",
             "Province/State": "state",
             "Lat": "latitude",
             "Long": "longitude"
             }
)

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
resourcedir = f"{homedir}/code/processing/raw_data_processing/annotation/"
datadir = f"{homedir}/data/global/covid/"

# Read table with ISO information
country_to_a3 = pd.read_csv(
    f"{resourcedir}JohnsHopkins-to-A3.csv",
    comment="#"
)
country_to_a3 = dict(
    zip(country_to_a3["Country/Region"], country_to_a3["alpha3"])
)
# Add iso_a3 abreviation for country and source
df= df.assign(
    iso_a3=[country_to_a3[x] for x in df["country"]],
    source="jhu"

)
# Turn all columns to lowercase
df.columns = map(str.lower, df.columns)

# Store new tidy data-frames
df.to_csv(
    f"{datadir}jhu_case-death-recovered_state_global.csv",
    index=False
)
