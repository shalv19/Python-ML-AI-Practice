
# coding: utf-8

# In[64]:


#Title = Assignment_work
#Date modified = 09/07/2018
#Author = Shalva Rai
#Description = import CSV file and do some modification
import pandas as pd
import numpy as np


# In[27]:


dt = pd.read_csv('C:\\Users\\shalv\\Downloads\\Iris.csv',index_col='Id')
dt.isnull().sum()


# In[46]:


df = pd.DataFrame(np.random.randn(100,5))  #create random dataset with random function
df


# In[47]:


df[df > 0.9] = pd.np.nan   #Put some random variable in the dataset.


# In[49]:


df.info()    #count the number of na value in the dataset.


# In[55]:


df_na = df.dropna() #drop the row with na value in it.
df_na.info()  


# In[56]:


df_fna = df.fillna(df.mean())
df_fna.info()


# In[70]:


test_list = ['a','b','c','d','2']
df_test = pd.DataFrame.from_records(test_list, columns=['my_list'])
df_test


# In[99]:


data = np.array([['row0','col1','col2'],['row1',2,5],['row2',6,7]])
data


# In[100]:


dfc = pd.DataFrame(data)


# In[101]:


dfc


# In[79]:


sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95]}
df = pd.DataFrame.from_dict(sales)


# In[80]:


df  #create dataframe from dict.


# In[102]:


dfc.columns = ['row_name','name1','name2']   #rename the column name in data set.


# In[103]:


dfc


# In[108]:


dummy_col = pd.Series(np.random.randn(3)) #generate random 3 row value for dummy_column.


# In[109]:


dfc = dfc.assign(dummy_col=dummy_col.values)   #assign the column to existing dataframe.


# In[107]:


dfc


# In[125]:


#Map and Lambda function example.
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)


# In[123]:


for i in F:
    print(i)


# In[130]:


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
for i in Fahrenheit:
    print(i)    # print Lambda function output.

