#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv('coaster_db.csv')

df.head()

#https://www.kaggle.com/code/robikscube/introduction-to-exploratory-data-analysis/notebook


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


# In[6]:


df.columns


# In[10]:


df.dtypes


# In[11]:


df.describe()


# In[51]:


df2 = df[['coaster_name', 
     #'Length', 'Speed', 
     'Location', 'Status', 
     #'Opening date',
       #'Type', 
     'Manufacturer',
     #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
      # 'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 
     'Opened', 
     #'Replaced by', 'Website',
      # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
      # 'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 
     'latitude', 'longitude', 
    'Type_Main',
       'opening_date_clean',
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
     #'height_value', 'height_unit', 
     'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[49]:


#dropping single column
#df.drop(['Opening date'], axis=1)
df.shape


# In[28]:


pd.to_datetime(df['opening_date_clean'])


# In[30]:


pd.to_numeric(df['year_introduced'])


# In[55]:


#rename oir columns
df2.rename(columns={'coaster_name':'Coaster_name',
              'year_introduced':'Year_introduced',
                  'pening_date_clean':'Oening_date_clean',
                  'speed_mph':'Speed_mph',
                  'height_ft':'Height_ft',
                  'Inversions_clean':'Inversions',
                  'Gforce_clean':'Gforce'})


# In[52]:


df2.isnull().sum()


# In[42]:


df.loc[df.duplicated()]


# In[45]:


#chech for duplicate coaster name
df.loc[df.duplicated(subset=['coaster_name'])].head(5)


# In[53]:


#cheacking an example duplicated
df2.query('coaster_name == "Crystal Beach Cyclone"')


# In[56]:


df2.columns


# In[65]:


df2.loc[~df2.duplicated(subset=['coaster_name','Location','opening_date_clean'])] \
    .reset_index(drop=True)


# In[66]:


df = df2.loc[~df2.duplicated(subset=['coaster_name','Location','opening_date_clean'])] \
    .reset_index(drop=True).copy()


# In[67]:


df.shape


# In[69]:


df.head()


# In[70]:


df['year_introduced'].value_counts()


# In[77]:


ax = df['year_introduced'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top year Coasters Introduce')
ax.set_xlabel('Year Introduce')
ax.set_ylabel('Count')


# In[79]:


df.head()


# In[84]:


ax = df['speed_mph'].plot(kind='hist', 
                     bins=20, 
                     title='Coaster speed')
ax.set_xlabel('Speed')
ax.set_ylabel('Frecuency')


# In[87]:


ax = df['speed_mph'].plot(kind='kde',                      
                     title='Coaster speed')
ax.set_xlabel('Speed')


# In[90]:


df.plot(kind='scatter', 
        x='speed_mph',
       y='height_ft',
       title='Coaster Speed v/s Height')

plt.show()


# In[91]:


import seaborn as sns


# In[95]:


sns.scatterplot( x='speed_mph',
       y='height_ft',
                hue='year_introduced',
               data=df)
plt.show()


# In[96]:


df.head()


# In[99]:


sns.pairplot(df, vars=['year_introduced', 'speed_mph', 'height_ft', 'Inversions_clean', 'Gforce_clean'],
            hue='Type_Main')
plt.show()


# In[105]:


df_corr = df[['year_introduced', 'speed_mph', 'height_ft', 'Inversions_clean', 'Gforce_clean']].dropna().corr()
df_corr


# In[108]:


sns.heatmap(df_corr, annot=True)
plt.show()


# In[109]:


#what are the location with the fastest roller coaster( with minimun of 10 )?


# In[115]:


ax = df.query('Location != "Other"') \
    .groupby('Location')['speed_mph'] \
    .agg(['mean', 'count']) \
    .query('count >= 10') \
    .sort_values('mean')['mean'] \
    .plot(kind='barh', figsize=(12, 5), title = 'Average Coast Speed by Location')

ax.set_xlabel('Average Coaster Speed')

plt.show()


# In[ ]:




