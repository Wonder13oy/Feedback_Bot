import pandas as pd

df = pd.read_csv('../assets/recruits.csv')
original_cols = df.columns

df = df[['Email Address', 'Your cohort ', 'Project instructions url part', 'Link to git repo']]
df.columns = ['email', 'cohort', 'project', 'repo']

# split cohort
cohorts = []
departments = []


def split_cohort(value):
    vals = value.split(' ')

    if len(vals) == 3:
        dpt = vals[1] + ' ' + vals[2]
        new_cohort = vals[0]
    else:
        new_cohort = vals[0].upper()
        dpt = vals[1]

    cohorts.append(new_cohort)
    departments.append(dpt.lower())


def clean_dataset():
    df['cohort'].apply(split_cohort)
    df['cohort'] = cohorts
    df['department'] = departments

    return df


df = clean_dataset()


def return_certain(value):
    if value == 'cohort':
        return sorted(df[value].unique())
    else:
        return df[value].unique().tolist()


def return_recruit_with(target, condition, value):
    recruit_info = df[df[condition] == value]
    return recruit_info[target].unique().tolist()
