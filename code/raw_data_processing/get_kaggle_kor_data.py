import git
import zipfile
import os
import pandas as pd

from kaggle.api.kaggle_api_extended import KaggleApi

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/kor/covid/"

# This requires a valid kaggle.json file in ~/.kaggle/
api = KaggleApi()
api.authenticate()
# Download the complete DS4C SK dataset
api.dataset_download_files(
    'kimjihoo/coronavirusdataset', path=datadir, force=True
)

#unzip dataset to destination
with zipfile.ZipFile(f"{datadir}coronavirusdataset.zip",'r') as zip_ref:
    zip_ref.extractall(datadir)

# Generate dictionary for file renaming
rename_dict = {
    "Case.csv": "kaggle_case_city_kor.csv",
    "PatientInfo.csv": "kaggle_patient-info_patient_kor.csv",
    "PatientRoute.csv": "kaggle_patient-route_patient_kor.csv",
    "Region.csv": "kaggle_province-demography_province_kor.csv",
    "SearchTrend.csv": "kaggle_search-trend_country_kor.csv",
    "SeoulFloating.csv": "kaggle_seoul-floating_city_kor.csv",
    "Time.csv": "kaggle_test-case-recovered-death_country_kor.csv",
    "TimeAge.csv": "kaggle_age-case-death_country_kor.csv",
    "TimeGender.csv": "kaggle_sex-case-death_country_kor.csv",
    "TimeProvince.csv": "kaggle_case-recovered-death_province_kor.csv",
    "Weather.csv": "kaggle_weather_province_kor.csv",
}

# Loop through files, rename files and columns
for old_file, new_file in rename_dict.items():
    print(new_file)
    # Check if old file exists
    if os.path.exists(f"{datadir}{old_file}"):
        # Rename file
        os.rename(f"{datadir}{old_file}", f"{datadir}{new_file}")
    # Read file into memory
    df = pd.read_csv(f"{datadir}{new_file}")
    # Change column names if necessary
    if "confirmed" in list(df.columns):
        df = df.rename(columns={"confirmed": "case"})
    if "deceased" in list(df.columns):
        df = df.rename(columns={"deceased": "death"})
    if "released" in list(df.columns):
        df = df.rename(columns={"released": "recovered"})
    if "released" in list(df.columns):
        df = df.rename(columns={"released": "recovered"})
    df = df.assign(source="kaggle", iso_a3="KOR")
    # Write file
    df.to_csv(f"{datadir}{new_file}", index=False)