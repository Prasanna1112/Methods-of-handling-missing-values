#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
data.isnull().sum()


# In[40]:


age_null = pd.isnull(data['Age'])
print(data[age_null])


# In[41]:


data["Age"].fillna(method='pad', inplace=True)
print(data["Age"])
# print(data.isnull().sum())


# In[43]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'].fillna(method='ffill', inplace=True)
# print(data['Age'])
print(data)


# In[38]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'].fillna(method='bfill', inplace=True)
print(data['Age'])


# In[45]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data["Age"].fillna(30, inplace = True)
print(data.head(30))


# In[50]:


import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data.replace(to_replace = np.nan, value = 1000, inplace=True)
print(data.head(30))


# In[51]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'].fillna(data['Age'].mean(), inplace=True)
print(data)


# In[53]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data.interpolate(method ='linear', limit_direction ='forward', inplace=True)
print(data.head(20))


# In[54]:


# Example of imputing missing values using scikit-learn
from numpy import nan
from numpy import isnan
from pandas import read_csv
from sklearn.impute import SimpleImputer

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",usecols=['Age'])

values = data.values

# define the imputer
imputer = SimpleImputer(missing_values=nan, strategy='mean')

transformed_values = imputer.fit_transform(values)

print('Missing: %d' % isnan(transformed_values).sum())


# In[58]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'].fillna(data['Age'].median(), inplace=True)
print(data['Age'].head(20))


# In[56]:


import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

data['Age'].fillna(data['Age'].mean(), inplace=True)
print(data)


# In[ ]:


import pandas as pd

data = pd.read_csv(r"C:\Users\balachandar.k\Desktop\New folder\titanic.csv")

new = data.dropna(how ='any')
# new = data.dropna(how ='all')
# new = data.dropna()

print(new)

