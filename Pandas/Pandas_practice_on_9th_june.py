
# coding: utf-8

# In[1]:


# Author = Shalva Rai
#Title = Pandas_practice_on_9th_june
#date modified = 9/07/2018
#Description = pandas practice in class.
import pandas as pd
import numpy as np


# In[7]:


df=pd.DataFrame({'num':[1,2,3,4,5]})
df['num'].map(lambda x:x+101)


# In[30]:


names=['Bob','Jessica','Mary','John','Mel']
birth=[968,155,77, 578, 973]
BabyDataSet = list(zip(names,birth))
print(BabyDataSet)


# In[15]:


ipl_data = {'Team':['Riders', 'Riders', 'Devils','Devils','Kings','Kings','Kings','Kings','Riders','Royals','Royals','Riders'],
                    'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],
                    'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
                    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)


# In[17]:


k= df.groupby('Team')
for i in k:
    print(i)


# In[20]:


#Data Visualization 
df.plot(x='Team',y='Year',kind='hist')


# In[21]:


df.plot(x='Team',y='Points',kind='line')


# In[22]:


df.plot(x='Team',y='Points',kind='bar')


# In[24]:


df.plot(x='Team',y='Points',kind='box')


# In[25]:


df1 = pd.DataFrame({
'id':[1,2,3,4,5],
'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
'subject_id':['sub1','sub2','sub4','sub6','sub5']})
df2 = pd.DataFrame(
{'id':[1,2,3,4,5],
'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
'subject_id':['sub2','sub4','sub3','sub6','sub5']})

print(df1)  #print the dataframe
print(df2)  


# In[26]:


print(pd.merge(df1,df2,on=['id','subject_id']))  #merge two dataframe with common attribute.


# In[27]:


print(pd.merge(df1, df2, on='subject_id', how='left'))  #Left join or merge of dataframe
print(pd.merge(df1, df2, on='subject_id', how='inner'))  #inner merge of dataframe


# In[3]:


users = pd.read_table('C:/Users/shalv/Downloads/emp_details.txt',sep='|',index_col='user_id')


# In[4]:


users.head(5)


# In[5]:


print(users.shape)


# In[6]:


print(users.columns)


# In[7]:


print(users.occupation)


# In[8]:


users.occupation.value_counts().head()


# In[9]:


users.occupation.unique()


# In[10]:


round(users.age.mean())


# In[11]:


users.iloc[1:7,1:]


# In[12]:


users[users['age']>50]


# In[13]:


users.groupby('occupation').size()


# In[17]:


captalizer = lambda x:x.upper()
print(users['occupation'].apply(captalizer))


# In[18]:


captalizer = lambda x:'male' if x == 'M' else 'female'
print(users['gender'].apply(captalizer))

