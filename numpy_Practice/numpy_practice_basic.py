
# coding: utf-8

# In[2]:


# Author = Shalva Rai
# Subject = numpy practice
# Date modified = 4/07/2018
import numpy as np


# In[3]:


print(np.__version__)


# In[9]:


a= np.array([2,3,5,'hi'])
a


# In[31]:


b = np.array([(2,5,7),(6,3,9)],dtype=int)
b


# In[10]:


c = np.array([[(2,5,7),(6,3,9)],[(2,5,7),(6,3,9)]])
c


# In[13]:


np.zeros((3,4),dtype=int)


# In[40]:


one=np.ones((2,3),dtype=np.int8)
one


# In[19]:


np.arange(10,25,1)


# In[23]:


# eqqual partion betweeen 10 to 30 in a line arrar
np.linspace(10,30,5)


# In[24]:


np.logspace(10,20,3)


# In[25]:


b.shape


# In[26]:


a.shape


# In[27]:


b.ndim #number of dimentionality.


# In[34]:


b.dtype.name
b.astype(float)


# In[41]:


b-one
np.subtract(b,one)


# In[43]:


b+one
np.add(b,one)


# In[44]:


np.sqrt(b)


# In[45]:


b==one


# In[46]:


#Slicing
a[0:2]


# In[50]:


i=np.transpose(b)
i


# In[4]:


np.full((3, 3), True, dtype=bool)


# In[5]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[6]:


arr[arr % 2 ==1]   #find odd number from array


# In[7]:


arr[arr % 2 ==0]   #find even number.


# In[9]:


#replace all odd number in arr with -1 or given number.
arr[arr % 2 ==1] = -1
arr


# In[13]:


#replace odd nuber without changing the original number.
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)


# In[16]:


#reshape the array 
arr.reshape(2,-1)  #setting to -1 automatically decides the number of cols


# In[17]:


arr.reshape(2,5)


# In[23]:


arr = np.arange(10)
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a)
print(b)
np.concatenate([a,b], axis=0)  #method #1.


# In[24]:


np.vstack([a,b]) #method #2.


# In[29]:


# Stack the arrays a and b horizontally.
a = np.arange(10).reshape(2,-1)

b = np.repeat(1, 10).reshape(2,-1)


# In[31]:


np.concatenate([a,b], axis = 1) #method #1.


# In[32]:


np.hstack([a, b])   #method #2.


# In[35]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9]) 
#From array a remove all items present in array b.
np.setdiff1d(a,b)


# In[38]:


#Swap rows 1 and 2 in the array arr.
arr1 = np.arange(9).reshape(3,3)
arr1[[1,0,2], :]


# In[39]:


#Reverse the rows of a 2D array arr.
arr1 = np.arange(9).reshape(3,3)
arr1[::-1]


# In[40]:


# Reverse the columns of a 2D array arr.
arr1[:, ::-1]

