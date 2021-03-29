#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    
    # Method chanin 1 (load data and rename columns)
    
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(columns={'age': 'AGE', 'sex': 'SEX', 'bmi': 'BMI', 'children': 'CHILDREN', 'smoker': 'SMOKER', 'region': 'REGION', 'charges': 'MEDICAL CHARGES'})
          )
    
    # Method chain 2 (Drop columns, round values and sort values)
    df2 = (
          df1
          .drop(['REGION'], axis=1)
          .round(2)
          .sort_values("AGE", ascending=True)
          )
    
    # Method chain 3 (Sort Data to locate smokers and style currency values)
    df3 = (
          df2
          .loc[lambda x: x['SMOKER'] == 'yes']
          .style.format({'MEDICAL CHARGES':'${0:,.2F}'})
          )
    
    return df3


# In[ ]:




