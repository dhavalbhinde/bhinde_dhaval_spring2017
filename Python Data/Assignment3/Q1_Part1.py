
# coding: utf-8

# In[82]:

import os
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass

df1=pd.read_csv("Assignment3\\Data\\vehicle_collisions.csv") # read CSV
print('complete')


# In[83]:

import datetime
datetime.datetime.strptime

df1['DATE']  = pd.to_datetime(df1['DATE'])
df_masked = df1[(df1['DATE'] >= datetime.date(2016,1,1))] # Extract data post 01/01/2016

print('complete')


# In[84]:

df2 = pd.DataFrame(index=range(12),columns=['Month','Manhattan','NYC','Percentage'])
df2['Month'] = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Filter data by Date and get accident by month and city

df_masked_jan = df1[(df1['DATE'] >= datetime.date(2016,1,1)) & (df1['DATE'] <= datetime.date(2016,1,31))]
accidents_jan_NY = len(df_masked_jan.index)
print('Accidents in NY Jan',accidents_jan_NY)

df_masked_jan_man = (df_masked_jan.loc[df_masked_jan['BOROUGH'] == 'MANHATTAN'])
accidents_jan_man = len(df_masked_jan_man.index)
print('Accidents in NY Jan Manhattan',accidents_jan_man)

percent_jan = accidents_jan_man/accidents_jan_NY
print('Percentage',percent_jan)


# In[85]:

# Filter data by Date and get accident by month and city

df_masked_feb = df1[(df1['DATE'] >= datetime.date(2016,2,1)) & (df1['DATE'] <= datetime.date(2016,2,29))]
accidents_feb_NY = len(df_masked_feb.index)
print('Accidents in NY Feb',accidents_feb_NY)

df_masked_feb_man = (df_masked_feb.loc[df_masked_feb['BOROUGH'] == 'MANHATTAN'])
accidents_feb_man = len(df_masked_feb_man.index)
print('Accidents in NY Feb Manhattan',accidents_feb_man)

percent_feb = accidents_feb_man/accidents_feb_NY
print('Percentage',percent_feb)


# In[86]:

# Filter data by Date and get accident by month and city

df_masked_mar = df1[(df1['DATE'] >= datetime.date(2016,3,1)) & (df1['DATE'] <= datetime.date(2016,3,31))]
accidents_mar_NY = len(df_masked_mar.index)
print('Accidents in NY mar',accidents_mar_NY)

df_masked_mar_man = (df_masked_mar.loc[df_masked_mar['BOROUGH'] == 'MANHATTAN'])
accidents_mar_man = len(df_masked_mar_man.index)
print('Accidents in NY mar Manhattan',accidents_mar_man)

percent_mar = accidents_mar_man/accidents_mar_NY
print('Percentage',percent_mar)


# In[87]:

# Filter data by Date and get accident by month and city

df_masked_apr = df1[(df1['DATE'] >= datetime.date(2016,4,1)) & (df1['DATE'] <= datetime.date(2016,4,30))]
accidents_apr_NY = len(df_masked_apr.index)
print('Accidents in NY apr',accidents_apr_NY)

df_masked_apr_man = (df_masked_apr.loc[df_masked_apr['BOROUGH'] == 'MANHATTAN'])
accidents_apr_man = len(df_masked_apr_man.index)
print('Accidents in NY apr Manhattan',accidents_apr_man)

percent_apr = accidents_apr_man/accidents_apr_NY
print('Percentage',percent_apr)


# In[88]:

# Filter data by Date and get accident by month and city

df_masked_may = df1[(df1['DATE'] >= datetime.date(2016,5,1)) & (df1['DATE'] <= datetime.date(2016,5,31))]
accidents_may_NY = len(df_masked_may.index)
print('Accidents in NY may',accidents_may_NY)

df_masked_may_man = (df_masked_may.loc[df_masked_may['BOROUGH'] == 'MANHATTAN'])
accidents_may_man = len(df_masked_may_man.index)
print('Accidents in NY may Manhattan',accidents_may_man)

percent_may = accidents_may_man/accidents_may_NY
print('Percentage',percent_may)


# In[90]:

# Filter data by Date and get accident by month and city

df_masked_jun = df1[(df1['DATE'] >= datetime.date(2016,6,1)) & (df1['DATE'] <= datetime.date(2016,6,30))]
accidents_jun_NY = len(df_masked_jun.index)
print('Accidents in NY jun',accidents_jun_NY)

df_masked_jun_man = (df_masked_jun.loc[df_masked_jun['BOROUGH'] == 'MANHATTAN'])
accidents_jun_man = len(df_masked_jun_man.index)
print('Accidents in NY jun Manhattan',accidents_jun_man)

percent_jun = accidents_jun_man/accidents_jun_NY
print('Percentage',percent_jun)


# In[91]:

# Filter data by Date and get accident by month and city

df_masked_jul = df1[(df1['DATE'] >= datetime.date(2016,7,1)) & (df1['DATE'] <= datetime.date(2016,7,31))]
accidents_jul_NY = len(df_masked_jul.index)
print('Accidents in NY jul',accidents_jul_NY)

df_masked_jul_man = (df_masked_jul.loc[df_masked_jul['BOROUGH'] == 'MANHATTAN'])
accidents_jul_man = len(df_masked_jul_man.index)
print('Accidents in NY jul Manhattan',accidents_jul_man)

percent_jul = accidents_jul_man/accidents_jul_NY
print('Percentage',percent_jul)


# In[92]:

# Filter data by Date and get accident by month and city

df_masked_aug = df1[(df1['DATE'] >= datetime.date(2016,8,1)) & (df1['DATE'] <= datetime.date(2016,8,31))]
accidents_aug_NY = len(df_masked_aug.index)
print('Accidents in NY aug',accidents_aug_NY)

df_masked_aug_man = (df_masked_aug.loc[df_masked_aug['BOROUGH'] == 'MANHATTAN'])
accidents_aug_man = len(df_masked_aug_man.index)
print('Accidents in NY aug Manhattan',accidents_aug_man)

percent_aug = accidents_aug_man/accidents_aug_NY
print('Percentage',percent_aug)


# In[93]:

# Filter data by Date and get accident by month and city

df_masked_sep = df1[(df1['DATE'] >= datetime.date(2016,9,1)) & (df1['DATE'] <= datetime.date(2016,9,30))]
accidents_sep_NY = len(df_masked_sep.index)
print('Accidents in NY sep',accidents_sep_NY)

df_masked_sep_man = (df_masked_sep.loc[df_masked_sep['BOROUGH'] == 'MANHATTAN'])
accidents_sep_man = len(df_masked_sep_man.index)
print('Accidents in NY sep Manhattan',accidents_sep_man)

percent_sep = accidents_sep_man/accidents_sep_NY
print('Percentage',percent_sep)


# In[94]:

# Filter data by Date and get accident by month and city

df_masked_oct = df1[(df1['DATE'] >= datetime.date(2016,10,1)) & (df1['DATE'] <= datetime.date(2016,10,31))]
accidents_oct_NY = len(df_masked_oct.index)
print('Accidents in NY oct',accidents_oct_NY)

df_masked_oct_man = (df_masked_oct.loc[df_masked_oct['BOROUGH'] == 'MANHATTAN'])
accidents_oct_man = len(df_masked_oct_man.index)
print('Accidents in NY oct Manhattan',accidents_oct_man)

percent_oct = accidents_oct_man/accidents_oct_NY
print('Percentage',percent_oct)


# In[96]:

# Filter data by Date and get accident by month and city

df_masked_nov = df1[(df1['DATE'] >= datetime.date(2016,11,1)) & (df1['DATE'] <= datetime.date(2016,11,30))]
accidents_nov_NY = len(df_masked_nov.index)
print('Accidents in NY nov',accidents_nov_NY)

df_masked_nov_man = (df_masked_nov.loc[df_masked_nov['BOROUGH'] == 'MANHATTAN'])
accidents_nov_man = len(df_masked_nov_man.index)
print('Accidents in NY nov Manhattan',accidents_nov_man)

percent_nov = accidents_nov_man/accidents_nov_NY
print('Percentage',percent_nov)


# In[97]:

# Filter data by Date and get accident by month and city

df_masked_dec = df1[(df1['DATE'] >= datetime.date(2016,12,1)) & (df1['DATE'] <= datetime.date(2016,12,31))]
accidents_dec_NY = len(df_masked_dec.index)
print('Accidents in NY dec',accidents_dec_NY)

df_masked_dec_man = (df_masked_dec.loc[df_masked_dec['BOROUGH'] == 'MANHATTAN'])
accidents_dec_man = len(df_masked_dec_man.index)
print('Accidents in NY dec Manhattan',accidents_dec_man)

percent_dec = accidents_dec_man/accidents_dec_NY
print('Percentage',percent_dec)


# In[98]:

# Update the 12 month data into a new dataframe

df2['Manhattan'] = [accidents_jan_man, accidents_feb_man, accidents_mar_man, accidents_apr_man, accidents_may_man,                     accidents_jun_man, accidents_jul_man, accidents_aug_man, accidents_sep_man, accidents_oct_man,                     accidents_nov_man, accidents_dec_man]

df2['NYC'] = [accidents_jan_NY, accidents_feb_NY, accidents_mar_NY, accidents_apr_NY, accidents_may_NY,                     accidents_jun_NY, accidents_jul_NY, accidents_aug_NY, accidents_sep_NY, accidents_oct_NY,                     accidents_nov_NY, accidents_dec_NY]

df2['Percentage'] = [percent_jan, percent_feb, percent_mar, percent_apr, percent_may, percent_jun, percent_jul,                      percent_aug, percent_sep, percent_oct, percent_nov, percent_dec]


# In[99]:

df2.to_csv("Assignment3\\Results\\P1.1_Results.csv", sep=',', encoding='utf-8')
df2.head()

