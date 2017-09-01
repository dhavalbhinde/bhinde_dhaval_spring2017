
# coding: utf-8

# In[125]:

import os
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass


df1=pd.read_csv("Assignment3\\Data\\employee_compensation.csv") #Read CSV



# In[126]:

df2 = df1[['Organization Group','Department','Total Compensation']] #Get required columns 


# In[127]:

df3 = df2.groupby(['Organization Group','Department']).mean() #Average the Total Compensation Grouped by Org & Dep


# In[128]:

df4 = df3.reset_index(drop=False)
df5 = df4.sort_values(by='Total Compensation', ascending=False) #Sort by Total Compensation
# test = df.sort('one', ascending=False)


# In[129]:

df6 = df5.groupby('Organization Group').head(1) # Find the Topmost Department Compensation for Every Org. Group
df6.to_csv("Assignment3\\Results\\P2.1_Results.csv", sep=',', encoding='utf-8')
df6.head()

