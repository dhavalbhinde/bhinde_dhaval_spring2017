
# coding: utf-8

# In[5]:

import os
import pandas as pd
import numpy as np

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass


df1=pd.read_csv("Assignment3\\Data\\cricket_matches.csv") #Read CSV
df2= df1[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] #Extract required column data

print("complete")


# In[6]:

df2 = df2[(df2["home"]==df2["winner"])]  # Extract data where Host Team is the Winner Team

df2_innings1 = df2[(df2["winner"]==df2["innings1"])]   # Get Innings1 data where Host Team has played Innings1
df2_innings2 = df2[(df2["winner"]==df2["innings2"])]   # Get Innings2 data where Host Team has played Innings2

df2_innings1 = df2_innings1[['winner','innings1_runs']]  # Extract required columns only
df2_innings2 = df2_innings2[['winner','innings2_runs']]  # Extract required columns only

df2_innings1.columns=['winner','runs']  #Re-assign column names for further reference
df2_innings2.columns=['winner','runs']  #Re-assign column names for further reference

df3 = pd.concat([df2_innings1,df2_innings2])  #Concatenate 2 dataframes to combine innings 1 & 2 data

df_x1 = df3.groupby(df3['winner']).mean()  # Get Average runs by Winner team

df_x1 = df_x1.reset_index()                #Restting index to get filtered data
df_x1.columns = ['Team','Average Runs']

df_x1.to_csv("Assignment3\\Results\\P3_Results.csv", sep=',', encoding='utf-8')
df_x1.head()



