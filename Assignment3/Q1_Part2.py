
# coding: utf-8

# In[1]:

import os
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass

df1=pd.read_csv("Assignment3\\Data\\vehicle_collisions.csv") #Read CSV
print('complete')


# In[2]:

#Extract Borough and Vehicle data only

df2 = df1[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]

#Sum up the data horizontally to get the no.of vehicles involved in each incident

df2['Count'] = df2[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]                .apply(lambda x: sum(x.notnull()), axis=1)
    


# In[3]:

# Create new dataframe containing the Borough and no.of vehicles involved in each accident

df3 = df2[['BOROUGH','Count']]
df4 = df3.groupby(['BOROUGH','Count']).size()


# In[4]:

#Reset index and re-assign column names for futher reference

df5 = df4.reset_index(drop=False)
df5.columns = ['Borough', 'vehicles', 'Count']


# In[5]:

#Pivot table to get the lateral view of data

df6 = df5.pivot_table('Count', ['Borough'], 'vehicles')
df7 = df6.reset_index(drop=False)


# In[6]:

#Re-assign column names for futher reference

df7.columns=['Borough','Zero','One','Two','Three','Four','Five']


# In[7]:

#Sum up the data for More than 3 vehicles involved data

df7['More_Vehicles_Involved'] = df7['Zero'] + df7['Four'] + df7['Five']


# In[8]:

#Remove unwanted columns

del df7['Zero']
del df7['Four']
del df7['Five']


# In[9]:

df7.columns=['Borough','One_Vehicle_Involved','Two_Vehicles_Involved','Three_Vehicles_Involved','More_Vehicles_Involved']
df7.head()


# In[10]:

df7.to_csv("Assignment3\\Results\\P1.2_Results.csv", sep=',', encoding='utf-8')

