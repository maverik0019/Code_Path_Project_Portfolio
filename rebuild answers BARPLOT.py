#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')

caffe.head(5)


# In[3]:


#replace Missing values should be replaced with 0. RATING
caffe['Rating'] = caffe['Rating'].fillna(0)   


# In[4]:


#replace Missing values should be replaced with the overall median.REVIEWS

import pandas as pd
import numpy as np

caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')
caffe2 = caffe["Reviews"].mean()
print(caffe2)


# In[5]:


#replace REVIEWS. Missing values should be replaced with the overall median.
caffe["Reviews"] = caffe["Reviews"].replace(np.nan,caffe2)
caffe.head(5)


# In[6]:


#Price Missing values should be replaced with ”Unknown
caffe["Price"] = caffe["Price"].replace(np.nan, "Unknown")


# In[7]:


#Delivery Option.Missing values should be replaced with False.
caffe["Delivery option"] = caffe["Delivery option"].replace(np.nan, "False")


# In[8]:


#Dine in Option.Missing values should be replaced with False.
import pandas as pd
import numpy as np

caffe["Dine in option"] = caffe["Dine in option"].replace('', "False")


# In[9]:


#Takeaway Option.Missing values should be replaced with False.
caffe["Takeout option"] = caffe["Takeout option"].replace('', "False")


# In[10]:


pip install missingno


# In[11]:


import missingno as msno
import matplotlib.pyplot as plt
msno.matrix(caffe)
plt.show()


# In[12]:


caffe.isna().sum()


# In[15]:


#replace Missing values should be replaced with 0. RATING
caffe['Rating'] = caffe['Rating'].fillna(0) 
caffe['Rating'].head()


# In[19]:


import pandas as pd
import numpy as np

caffe["Dine in option"] = caffe["Dine in option"].replace(np.nan, "False")
caffe["Dine in option"].head(5)


# In[20]:


caffe


# In[23]:


#Takeaway Option.Missing values should be replaced with False.

caffe["Takeout option"] = caffe["Takeout option"].replace(np.nan, "False")
caffe["Takeout option"].head(100)


# In[24]:


caffe.isna().sum()


# In[25]:


caffe.isnull().sum()


# In[31]:


caffe.head()


# In[15]:


#get unique entires across multiple columns
caffe['Place type'].unique()


# In[14]:


import pandas as pd
import numpy as np


caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')

caffe_unique = caffe['Place name'].unique()


# In[10]:


caffe


# In[19]:


pd.value_counts(df['Place name'].values)


# In[22]:


df['Place name'].nunique()


# In[23]:


#Count distinct values, use nunique:
df['Place name'].count()


# In[25]:


# counting the duplicates
dups = df.pivot_table(index = ['Place name'], aggfunc ='size')

print(dups)


# In[1]:


#dups = df.pivot_table(index = ['Place name'], aggfunc ='size')

#print(dups)


# In[6]:


import pandas as pd
import numpy as np

caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')

caffe.head(5)


# In[10]:


caffe['Price'].unique()


# In[12]:


caffe['Price'].nunique()


# In[20]:


#range of values 
caffe['Price'].rank(
)


# In[23]:


#max ox range in a column
#df ['puntos']. max ()

caffe_rangemax = caffe['Rating'].max()
caffe_range


# In[25]:


caffe_rangemin = caffe['Rating'].min()
caffe_rangemin


# In[26]:


caffe_range = caffe['Rating'].max() - caffe['Rating'].min()
caffe_range


# In[37]:


#barplot 
#import matplotlib.pyplot as plt


#caffe['Place type'].plot(kind='bar', y='count', x='Places', color='red', rot=90)

#plt.show()

#pd.value_counts(df['Place name'].values)
import pandas as pd
import numpy as np


caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')
caffe.columns


# In[43]:


caffe_bar = pd.value_counts(caffe['Place type'].values)
caffe_bar


# In[54]:


import matplotlib.pyplot as plt


#caffe_bar.plot(kind='bar',
            #   y='count', 
           #    x='Places',
            #   color='red',
          #     rot=90

fig = caffe_bar.plot(kind='bar')
fig.set_title('Different stores')
fig.set_xlabel('Coffe Place type')
fig.set_ylabel('Frequency')
plt.grid()

              

plt.show()


# In[4]:


#import pandas as pd
#import seaborn as sns 
#import numpy as np
#import matplotlib.pyplot as plt

#caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')

#caffe.columns


# In[12]:


#import pandas as pd
#import seaborn as sns 
#import numpy as np
#import matplotlib.pyplot as plt

"""coffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')"""

"""



df = sns.load_dataset('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')
sns.boxplot(x=coffe["Place name"])
"""


# In[14]:


import seaborn as sns 


# In[20]:


caffe = pd.read_csv('https://s3.amazonaws.com/talent-assets.datacamp.com/coffee.csv')

caffe.head(5)


# In[28]:


import seaborn as sns 

sns.__version__


# In[32]:


sns.get_dataset_names()


# In[30]:


df = sns.load_dataset("titanic")
sns.boxplot(x=df["age"])


# In[33]:


import pandas as pd

from matplotlib import pyplot as plt

import seaborn as sb


# In[2]:


caffe = sns.load_dataset('caffe')
print(caffe.head())


# In[ ]:




