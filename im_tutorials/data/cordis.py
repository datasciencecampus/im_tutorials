from smart_open import smart_open
import pandas as pd
import ast

S3_PATH = 'https://s3.us-east-2.amazonaws.com/innovation-mapping-tutorials/{}'

def _projects_h2020_fp6(key):
    file_path = S3_PATH.format(key)
    df = pd.read_csv(
        smart_open(file_path),
        sep=';',
        encoding='iso-8859-1',
        parse_dates=['startDate', 'endDate'],
        infer_datetime_format=True,
        decimal=','
    )
    df['organisations'] = (df['coordinator'] + ';' +  df['participants']).fillna(df['coordinator'])
    df['countries'] = (df['coordinatorCountry'] + ';' +  df['participantCountries']).fillna(df['coordinatorCountry'])
    list_cols = ['organisations', 'countries', 'participants', 'participantCountries', 'programme']
    for col in list_cols:
        df[col] = df[col].str.split(';')

    df['startYear'] = df['startDate'].dt.year
    df['endYear'] = df['endDate'].dt.year
    return df

def _organizations_h2020_fp6(key):
    df = pd.read_csv(
        smart_open(S3_PATH.format(key)),
	sep=';',
	encoding='iso-8859-1',
	decimal=',',
    )
    return df

def _reports_h2020_fp6(key):
    df = pd.read_csv(
        smart_open(S3_PATH.format(key)),
        parse_dates=['lastUpdateDate'],
        infer_datetime_format=True,
    )
    df['lastUpdatedDateYear'] = df['lastUpdateDate'].dt.year
    return df

def h2020_projects():
    key = 'cordis/h2020/cordis-h2020projects.csv'
    return _projects_h2020_fp6(key)

def fp7_projects():
    key = 'cordis/fp7/cordis-fp7projects.csv'
    return _projects_h2020_fp6(key)

def fp6_projects():
    key = 'cordis/fp6/cordis-fp6projects.csv'
    return _projects_h2020_fp6(key)

def h2020_organizations():
    key = 'cordis/h2020/cordis-h2020organizations.csv'
    return _organizations_h2020_fp6(key)

def fp7_organizations():
    key = 'cordis/fp7/cordis-fp7organizations.csv'
    return _organizations_h2020_fp6(key)

def fp6_organizations():
    key = 'cordis/fp6/cordis-fp6organizations.csv'
    return _organizations_h2020_fp6(key)

def h2020_reports():
    key = 'cordis/h2020/cordis-h2020reports.csv'
    return _reports_h2020_fp6(key)

def fp7_reports():
    key = 'cordis/fp7/cordis-fp7reports.csv'
    return _reports_h2020_fp6(key)

### REFERENCE DATA ###
def reference_activity_type():
    key = 'cordis/ref/cordisref-organizationActivityType.csv'
    df = pd.read_csv(
    smart_open(S3_PATH.format(key)),
    sep=';'
    )
    return df

def reference_countries():
    key = 'cordis/ref/cordisref-countries.csv'
    df = pd.read_csv(
    smart_open(S3_PATH.format(key)),
    sep=';'
    )
    return df

def reference_funding_schemes():
    key = 'cordis/ref/cordisref-projectFundingSchemeCategory.csv'
    df = pd.read_csv(
    smart_open(S3_PATH.format(key)),
    sep=';'
    )
    return df

def reference_sic_codes():
    key = 'cordis/ref/cordisref-sicCode.csv'
    df = pd.read_csv(
    smart_open(S3_PATH.format(key)),
    sep=';'
    )
    df = df[df['language'] == 'en']
    df.drop('language', axis=1, inplace=True)
    return df
