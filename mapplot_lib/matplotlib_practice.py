
# coding: utf-8

# In[14]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style


# In[5]:


plt.plot([1,2,3,4],[4,5,1,8])
plt.show()


# In[7]:


x=[3,6,7]
y=[2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[15]:


x=[3,6,7]
y=[2,16,4]
x2=[6,9,11]
y2=[3,15,7]
plt.plot(x,y,'b',label='one line', linewidth=7)
plt.plot(x2,y2,'r', label='one line', linewidth=2)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[ ]:


population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,]

