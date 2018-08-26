
# coding: utf-8

# In[2]:


#Author = Shalva Rai
#Date Modified = 6/07/2018
#Subject = pandas package practice session 
import pandas as pd
import numpy as np


# In[3]:


arr=np.array([10,20,30])
arr


# In[4]:


pd.DataFrame(arr)


# In[7]:


s=pd.Series([19,25,33,47,53], index=[101,102,103,104,105])
s


# In[110]:


s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s[['a','c','d']]) #Retrive multiple elements from dataframe.


# In[112]:


data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['name','Age'],dtype=float)
print(df)


# In[114]:


data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)                               
                               


# In[115]:


ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)


# In[117]:


k = df.groupby('Team') 
for i in k:
    print(i)
#Printing the team details with for loop.


# In[119]:


df.plot(x='Team',y='Year',kind='hist') #plot the dataset in the hostram.


# In[120]:


df1 = pd.DataFrame({
'id':[1,2,3,4,5],
'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
'subject_id':['sub1','sub2','sub4','sub6','sub5']})
df2 = pd.DataFrame(
{'id':[1,2,3,4,5],
'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(df1)
print(df2)


# In[122]:


print(pd.merge(df1,df2,on=['id','subject_id'])) #merge using the id and subject_id.


# In[124]:


# merging methods 'How'
print('Merge using left outer join\n')
print(pd.merge(df1, df2, on='subject_id', how='left'))
print('Merge uging inner outer join\n')
print(pd.merge(df1, df2, on='subject_id', how='inner'))


# In[125]:


#Merge using Zip methods.
names=['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
BabyDataSet


# In[8]:


#Add, Subtract, multiply aand Divide two series.
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


# In[9]:


df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)  #print data frame from the key-value pair


# In[45]:


exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index=labels)
print(df) #Add multiple list to form a Data frame.


# In[46]:


print("Summary of the basic infprmation about this dataframe and its data:")
print(df.info()) #print summary of dataframe.


# In[67]:


#Select 'name' and 'score' columns from the dataframe.
print("Select the specific column:")
print(df[['name', 'score']])


# In[48]:


#Select the specified columns and rows from a given data frame.
#Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.

print(df.iloc[[1,3,5,6],[1,3]])  #[[row number],[col number]] to print the data from data frame


# In[49]:


#Select the rows where the number of attempts in the examination is greater than 2.
print(df.ix[[1,3,5]])


# In[50]:


#Select the rows where the score is missing, i.e. is NaN.

print(df[df['score'].isnull()])


# In[58]:


#Change the score in row 'd' to 11.5.
df.loc['d','score']=11.5
df


# In[62]:


#Sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
df.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sort the dataframe first by 'name' in descending order and then score in ascending order:")
print(df)


# In[70]:


#Replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
print("\nReplace the ‘qualify' column contains the values 'yes' and 'no'  with True and  False:")
df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
print(df)


# In[25]:


data=pd.read_csv('C:\\Users\\shalv\\Downloads\\Iris.csv', index_col='Id')


# In[13]:


data.head(7)


# In[21]:


data[:3].head(5)


# In[19]:


data.columns


# In[71]:


data.describe()


# In[86]:


users = pd.read_csv('C:\\Users\\shalv\\Downloads\\emp_details.txt',sep='|',index_col='user_id')
print('head\n',users.head(5))
print('tails\n',users.tail(5))
print(users.describe())


# In[91]:


print(users.shape[1])  #number of column
users.shape[0]  #number of rows


# In[94]:


print(set(users.occupation)) #set will give you unique occupation name.


# In[96]:


users.occupation.unique() #List the occupation in the data set in a array.


# In[97]:


users.age.mean() #Mean of user age.


# In[98]:


users.iloc[1:7,1:]  #Slicing and indexing.


# In[100]:


users[users['age']>50]   #Age greater than 50


# In[102]:


users.groupby('occupation').size()  #Groupby with count of occupation.


# In[105]:


captalizer = lambda x:x.upper() #function to make object in captial letter.
print(users['occupation'].apply(captalizer))


# In[106]:


captalizer = lambda x:'male' if x=='M' else 'female'
print(users['gender'].apply(captalizer))

