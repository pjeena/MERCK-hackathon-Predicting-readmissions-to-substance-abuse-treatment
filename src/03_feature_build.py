import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns', None)

from src.utils import MappingData
from sklearn.impute import SimpleImputer


path = os.path.join('data', 'treatments_2017-2020_preprocessed')

df = pd.read_parquet( path + '.parquet')
print(df.shape)

## here we encode data which is ordinal such as AGE, 

categories = ['12-17 years old', '18-29 years old', '30-39 years old', '40-49 years old', '50-64 years old', '65+ years old']
df['AGE'] = pd.Categorical(df['AGE'], categories= categories    , ordered=True)
labels,categories = pd.factorize( df['AGE'], sort = True)
df['AGE'] = labels


categories = ['No schooling', 'Grades 9-11', 'Grade 12', '1-3 years of college', '4 years of college, BA/BS, or more']
df['EDUC'] = pd.Categorical(df['EDUC'], categories= categories, ordered=True)
labels,categories = pd.factorize( df['EDUC'], sort = True)
df['EDUC'] = labels.astype(int)



categories = ['None', 'Once', 'Two or more times']
df['ARRESTS'] = pd.Categorical(df['ARRESTS'], categories= categories, ordered=True)
labels,categories = pd.factorize( df['ARRESTS'], sort = True)
df['ARRESTS'] = labels



categories = ['0-14 days', '15-30 days', '31+ days']
df['DAYWAIT'] = pd.Categorical(df['DAYWAIT'], categories= categories, ordered=True)
labels,categories = pd.factorize( df['DAYWAIT'], sort = True)
df['DAYWAIT'] = labels



categories = ['11 years and under', '12-17 years', '18-24 years', '25-29 years', '30 years and older']
df['FRSTUSE1'] = pd.Categorical(df['FRSTUSE1'], categories= categories, ordered=True)
labels,categories = pd.factorize( df['FRSTUSE1'], sort = True)
df['FRSTUSE1'] = labels



# creating a column for no of substances for each patient
categories = ['Zero sub', 'One sub', 'Two sub', 'Three sub']
df['NUM_SUBS'] = pd.Categorical(df['NUM_SUBS'], categories= categories, ordered=True)
labels,categories = pd.factorize( df['NUM_SUBS'], sort = True)
df['NUM_SUBS'] = labels




# selecting only features which we will use further
columns_of_imp = [
    "AGE",
    "GENDER",
    "RACE",
    "ETHNIC",
    "MARSTAT",
    "EDUC",
    "EMPLOY",
    "PREG",
    "VET",
    "LIVARAG",
    "PRIMINC",
    "ARRESTS",
    "DIVISION",
    "SERVICES",
    "DAYWAIT",
    "PSOURCE",
    "SUB1",
    "FREQ1",
    "FRSTUSE1",
    "PSYPROB",
    "HLTHINS",
    "FREQ_ATND_SELF_HELP",
    "NOPRIOR",
    "NUM_SUBS",
]
df = df[columns_of_imp]



# Dropping columns with more than 50% values
df_missing_perc = pd.DataFrame(df.isnull().sum()/df.shape[0] * 100 ).reset_index()
df_missing_perc.columns = ['Column', '% missing']
columns_50perc_missing = list( df_missing_perc[ df_missing_perc['% missing'] > 50.0 ]['Column'].values)
print(columns_50perc_missing)
df = df.drop(columns_50perc_missing, axis=1)



# Imputing missing values
imputer = SimpleImputer(missing_values = None, strategy='most_frequent')
df_transformed= pd.DataFrame( imputer.fit_transform(df),  columns = df.columns ).astype(df.dtypes.to_dict())



#df_transformed['AGE'] = df_transformed['AGE'].astype(int)
#f_transformed['EDUC'] = df_transformed['EDUC'].astype(int)
#df_transformed['ARRESTS'] = df_transformed['ARRESTS'].astype(int)
#df_transformed['DAYWAIT'] = df_transformed['DAYWAIT'].astype(int)
#df_transformed['FRSTUSE1'] = df_transformed['FRSTUSE1'].astype(int)
#df_transformed['NUM_SUBS'] = df_transformed['NUM_SUBS'].astype(int)

path_to_train = os.path.join('data', 'treatments_2017-2020' + '_train' + '.parquet')
df_transformed.to_parquet(path_to_train)