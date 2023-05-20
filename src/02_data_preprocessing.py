import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns', None)

from src.utils import MappingData



path = os.path.join('data', 'treatments_2017-2020')

df = pd.read_parquet( path + '.parquet')
print(df.shape)

# dropping rows where SUB1 is unknown
df = df[df['SUB1'] != 1].reset_index(drop=True)
df = df[df['NOPRIOR'] != -9].reset_index(drop=True)



## Mapping the features to their respective categories. 
mapping_obj = MappingData()

df['AGE'] = df['AGE'].apply(lambda x : mapping_obj.mapping_AGE(x))
df['GENDER'] = df['GENDER'].apply(lambda x : mapping_obj.mapping_GENDER(x))
df['RACE'] = df['RACE'].apply(lambda x : mapping_obj.mapping_RACE(x))
df['ETHNIC'] = df['ETHNIC'].apply(lambda x : mapping_obj.mapping_ETHNIC(x))

df['MARSTAT'] = df['MARSTAT'].apply(lambda x : mapping_obj.mapping_MARSTAT(x))
df['EDUC'] = df['EDUC'].apply(lambda x : mapping_obj.mapping_EDUC(x))
df['EMPLOY'] = df['EMPLOY'].apply(lambda x : mapping_obj.mapping_EMPLOY(x))
df['PREG'] = df['PREG'].apply(lambda x : mapping_obj.mapping_PREG(x))

df['VET'] = df['VET'].apply(lambda x : mapping_obj.mapping_VET(x))
df['LIVARAG'] = df['LIVARAG'].apply(lambda x : mapping_obj.mapping_LIVARAG(x))
df['PRIMINC'] = df['PRIMINC'].apply(lambda x : mapping_obj.mapping_PRIMINC(x))
df['ARRESTS'] = df['ARRESTS'].apply(lambda x : mapping_obj.mapping_ARRESTS(x))

df['DIVISION'] = df['DIVISION'].apply(lambda x : mapping_obj.mapping_DIVISION(x))
df['SERVICES'] = df['SERVICES'].apply(lambda x : mapping_obj.mapping_SERVICES(x))
df['DAYWAIT'] = df['DAYWAIT'].apply(lambda x : mapping_obj.mapping_DAYWAIT(x))
df['PSOURCE'] = df['PSOURCE'].apply(lambda x : mapping_obj.mapping_PSOURCE(x))

df['SUB1'] = df['SUB1'].apply(lambda x : mapping_obj.mapping_SUB(x))
df['FREQ1'] = df['FREQ1'].apply(lambda x : mapping_obj.mapping_FREQ(x))
df['FRSTUSE1'] = df['FRSTUSE1'].apply(lambda x : mapping_obj.mapping_FRSTUSE(x))
df['PSYPROB'] = df['PSYPROB'].apply(lambda x : mapping_obj.mapping_PSYPROB(x))

df['HLTHINS'] = df['HLTHINS'].apply(lambda x : mapping_obj.mapping_HLTHINS(x))
df['FREQ_ATND_SELF_HELP'] = df['FREQ_ATND_SELF_HELP'].apply(lambda x : mapping_obj.mapping_FREQ_ATND_SELF_HELP(x))
df['NOPRIOR'] = df['NOPRIOR'].apply(lambda x : mapping_obj.mapping_NOPRIOR(x))


df['NUM_SUBS'] = df.filter(regex='FLG$', axis = 1).sum(axis=1)
df['NUM_SUBS'] = df['NUM_SUBS'].apply(lambda x : mapping_obj.mapping_NUM_SUBS(x))



path = os.path.join('data' , 'treatments_2017-2020'+ '_preprocessed' + '.parquet')
df.to_parquet(path)

print(df.shape)