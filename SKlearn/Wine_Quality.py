
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib


# In[6]:


dataset_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')


# In[7]:


data.shape


# In[8]:


data.head()


# In[9]:


print(data.describe())


# In[10]:


data['quality'].unique()


# In[30]:


y= data.quality
X = data.drop('quality', axis=1)
X.head()


# In[31]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,
                                                    random_state=123,
                                                   stratify=y)


# In[32]:


pipeline = make_pipeline(preprocessing.StandardScaler(),
                        RandomForestRegressor(n_estimators=100))


# In[33]:


hyperparameters = {'randomforestregressor_max_features':['auto','sqrt','log2'],
                 'randomforestregressor_max_depth':[None,5,3,1]}


# In[36]:


clf = GridSearchCV(pipeline,hyperparameters, cv=10,n_jobs=1)


# In[37]:


clf.fit(X_train, y_train)


# In[27]:


pred = clf.predict(x_test)
print(r2_score(y_test, pred))
print(mean_squared_error(y_test,pred))

