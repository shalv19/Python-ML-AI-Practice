
# coding: utf-8

# In[1]:


#Import library file 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np


# In[2]:


# Read data from the system
model = pd.read_csv('Model.csv')
model.head()


# In[3]:


# From data set we need only Size, total_sqft,bath,balcony and price.
size = model['size'].values
total_sqft = model['total_sqft'].values
bath = model['bath'].values
balcony = model['balcony'].values
price = model['price'].values

dataset = pd.DataFrame({'size':size,'total_sqft':total_sqft,'bath':bath,
                       'balcony':balcony,'price':price})


# In[5]:


# Dataset without nan value 
print(dataset.isna().sum())
dataset = dataset.dropna()
print(dataset.isna().sum())
#Print the dataset discription.
print(dataset.describe())


# In[7]:


#Split the column to remove the text part in size column field and total_sqft should be cleaned.
dataset['size'] = dataset['size'].str.split(' ',1).str[0]
dataset['total_sqft'] = dataset['total_sqft'].str.split('-',1).str[0]
print(dataset.head())

# Now Data is prepared to fit in model


# In[15]:


# Create Liner rigression model for the dataset.
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

m = len(dataset)

# predict price with respect to size of bedroom.

X = dataset[['size','total_sqft','bath']]
Y = np.array(dataset['price'].values)

X = X.reshape((m,1))

reg = LinearRegression()

reg = reg.fit(X, Y)

Y_pred = reg.predict(X)

mse = mean_squared_error(Y, Y_pred)
rmse = np.sqrt(mse)
r2_score = reg.score(X, Y)

print("RMSE =",rmse)
print("R2_Score =",r2_score)

print('Predict price of 3 BHK:',reg.predict(3))

