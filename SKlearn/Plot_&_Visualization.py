
# coding: utf-8

# In[30]:


# Author = Shalva Rai
# Date created = 11/07/2018
# Title = plot and Visualization of data
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


df = pd.read_csv('C:\\Users\\shalv\\Downloads\\pokemon.csv',index_col=0)


# In[21]:


df.head()


# In[22]:


sns.lmplot(x='Attack',y='Defense',data=df)  #recommended way to plot the graph


# In[24]:


sns.boxplot(data=df)


# In[25]:


sns.violinplot(x='Type 1',y='Attack',data=df)


# In[29]:


import seaborn as sns

