
# coding: utf-8

# In[117]:

import os
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

try:
    os.chdir('C:/Users/Dhaval/Python_Data/bhinde_dhaval_spring2017/') # making changes to cwd for local reference
except:
    pass


df1=pd.read_csv("Assignment3\\Data\\employee_compensation.csv") #Read CSV
df1 = df1.loc[df1['Year Type'] == 'Calendar'] # Filter out fiscal year data



# In[118]:

#Get mean of all salaries for every employee

df2 = df1[['Employee Identifier','Job Family','Salaries','Overtime','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits','Total Benefits',     'Total Compensation']].groupby(['Employee Identifier','Job Family']).mean()


# In[119]:

# Find Employees whose overtime salaries are greater than 5% of Salaries

df3 = df2[df2['Overtime'] > 0.05*df2['Salaries']]


# In[120]:

#Reset Index

df3 = df3.reset_index(drop=False)


# In[121]:

#Extract required columns only

df4 = df3[['Job Family','Total Benefits','Total Compensation']]


# In[122]:

# Calculcate mean of 'Total Benefits','Total Compensation' grouped by Job Family.

df5 = df4.groupby(['Job Family']).mean()


# In[123]:

df5['Percent_Total_Benefit'] = df5['Total Compensation'] / df5['Total Benefits'] # Calculate Percent Benefit
df5.head()


# In[124]:

df5.to_csv("Assignment3\\Results\\P2.2_Results.csv", sep=',', encoding='utf-8') #Write to CSV

