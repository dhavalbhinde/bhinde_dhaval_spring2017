
# coding: utf-8

# In[113]:

import os
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass


df1=pd.read_csv("Assignment3\\Data\\movies_awards.csv") #Read CSV
df2=df1[['Awards']] #Extarct Raw Awards String data

#Use Regex string pattern to extract Won and Nominated Awards data

df2['Awards_won'] = df2['Awards'].str.extract('(\d+\swin)', expand=True)
df2['Awards_won'] = df2['Awards_won'].str.extract('(\d+)', expand=True)

df2['Awards_nominated'] = df2['Awards'].str.extract('(\d+\snomination)', expand=True)
df2['Awards_nominated'] = df2['Awards_nominated'].str.extract('(\d+)', expand=True)

df2['Oscar_Awards_nominated'] = df2['Awards'].str.extract('(Nominated\sfor\s\d+\sO)', expand=True)
df2['Oscar_Awards_nominated'] = df2['Oscar_Awards_nominated'].str.extract('(\d+)', expand=True)

df2['Oscar_Awards_won'] = df2['Awards'].str.extract('(Won\s\d+\sO)', expand=True)
df2['Oscar_Awards_won'] = df2['Oscar_Awards_won'].str.extract('(\d+)', expand=True)

df2['BAFTA_Awards_nominated'] = df2['Awards'].str.extract('(Nominated\sfor\s\d+\sB)', expand=True)
df2['BAFTA_Awards_nominated'] = df2['BAFTA_Awards_nominated'].str.extract('(\d+)', expand=True)

df2['BAFTA_Awards_won'] = df2['Awards'].str.extract('(Won\s\d+\sB)', expand=True)
df2['BAFTA_Awards_won'] = df2['BAFTA_Awards_won'].str.extract('(\d+)', expand=True)

df2['Golden_Globe_Awards_nominated'] = df2['Awards'].str.extract('(Nominated\sfor\s\d+\sG)', expand=True)
df2['Golden_Globe_Awards_nominated'] = df2['Golden_Globe_Awards_nominated'].str.extract('(\d+)', expand=True)

df2['Golden_Globe_Awards_won'] = df2['Awards'].str.extract('(Won\s\d+\sG)', expand=True)
df2['Golden_Globe_Awards_won'] = df2['Golden_Globe_Awards_won'].str.extract('(\d+)', expand=True)

df2['Primetime_Emmy_Awards_nominated'] = df2['Awards'].str.extract('(Nominated\sfor\s\d+\sP)', expand=True)
df2['Primetime_Emmy_Awards_nominated'] = df2['Primetime_Emmy_Awards_nominated'].str.extract('(\d+)', expand=True)

df2['Primetime_Emmy_Awards_won'] = df2['Awards'].str.extract('(Won\s\d+\sP)', expand=True)
df2['Primetime_Emmy_Awards_won'] = df2['Primetime_Emmy_Awards_won'].str.extract('(\d+)', expand=True)

print('complete')


# In[114]:

# Convert String to Numeric

df2[['Awards_won','Awards_nominated','Oscar_Awards_nominated','Oscar_Awards_won','BAFTA_Awards_nominated','BAFTA_Awards_won',
      'Golden_Globe_Awards_nominated','Golden_Globe_Awards_won','Primetime_Emmy_Awards_nominated',
    'Primetime_Emmy_Awards_won']] = df2[['Awards_won','Awards_nominated','Oscar_Awards_nominated','Oscar_Awards_won','BAFTA_Awards_nominated','BAFTA_Awards_won',
      'Golden_Globe_Awards_nominated','Golden_Globe_Awards_won','Primetime_Emmy_Awards_nominated',
    'Primetime_Emmy_Awards_won']].apply(pd.to_numeric)


# In[115]:

#Summing up Awards Won & Nominated

df2['Awards_won'] = df2.fillna(0)['Awards_won'] + df2.fillna(0)['Oscar_Awards_won'] + df2.fillna(0)['BAFTA_Awards_won']                     + df2.fillna(0)['Golden_Globe_Awards_won'] + df2.fillna(0)['Primetime_Emmy_Awards_won']
    
df2['Awards_nominated'] = df2.fillna(0)['Awards_nominated'] + df2.fillna(0)['Oscar_Awards_nominated'] +                           df2.fillna(0)['BAFTA_Awards_nominated'] + df2.fillna(0)['Golden_Globe_Awards_nominated'] +                           df2.fillna(0)['Primetime_Emmy_Awards_nominated']


# In[118]:

df2 = df2[pd.notnull(df2['Awards'])]
df2 = df2.fillna(0)
df2 = df2.reset_index()
del df2['index']


# In[120]:

df2.to_csv("Assignment3\\Results\\P4_Results.csv", sep=',', encoding='utf-8')

