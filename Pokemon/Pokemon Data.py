#!/usr/bin/env python
# coding: utf-8

# # Pokemon Data
# 

# In[13]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv')

print(poke.head(5))


# In[14]:


#columns
print(df.columns)


# In[15]:


print(df['Name'][0:5])


# In[17]:


#read each Column
print(df[['Name', 'Type 1', 'HP']])


# In[18]:


#read each row
print(df.iloc[1:4])


# In[20]:


#Read a specific LOcation( R,C)
#0 first column
print(df.iloc[2,1])  #secon rol first position


# In[24]:


#read each row
for index, row in df.iterrows():
    print(index, row['Name'])


# In[25]:


#read each row
df.loc[df['Type 1'] == "Fire"]  #find specific data in dataset(specific rows)


# # SORTING/DESCRIBIG DATA

# In[28]:


df.sort_values('Name', ascending=False)


# In[30]:


df.sort_values(['Type 1', 'HP'], ascending=True)


# In[32]:


df.sort_values(['Type 1', 'HP'], ascending=[1,0])# primera columna(Type 1) es ascending y la otra descending


# # Making Changes to the data 

# In[33]:


df.head()


# In[34]:


df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
df.head(5)


# In[37]:


df = df.drop(columns=['Total'])


# In[39]:


df['Total'] = df.iloc[:, 4:10].sum(axis=1)
df.head()


# In[41]:


cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
df.head()


# # Saving our Data ( Exporting into Desired Format)
# 

# In[55]:


df.to_csv('modified.csv', index=False)
#df.to_excel('modified.xlsx', index=False)
#df.to_txt('modified.txt', index=False, sep='\t')


# # Filtering Data

# In[56]:


df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]


# In[57]:


df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]


# In[60]:


df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] 


# In[61]:


new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] 


# In[62]:


new_df


# In[64]:


new_df.to_csv('filtered.csv')


# In[65]:


new_df = new_df.reset_index()
new_df


# In[72]:


new_df.reset_index(drop=True, inplace=True)
new_df= new_df.drop(columns=['index'])
new_df


# # Filtering Data Strings
# 
# df.loc[df['Name'].str.contains('Mega')]

# In[76]:


df.loc[df['Name'].str.contains('Mega')].head(5)


# In[77]:


df.loc[~df['Name'].str.contains('Mega')].head(5)


# In[81]:


import re
df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]


# In[83]:


#ignorando la capitalizacion de las letras. EL tamaño
df.loc[df['Type 1'].str.contains('Fire|Grass', flags=re.I, regex=True)]


# # Todos los pokemon que comienzan con PY

# In[85]:


#comienza con pi pi[a-z]* means zero o more
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]


# # Conditional Changes

# In[93]:


df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
df


# In[94]:


df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
df


# In[101]:


df.loc[df['Total'] > 500 , ['Geeration', 'Legendary']] = 'Test Value'
df


# In[102]:


df.loc[df['Total'] > 500 , ['Geeration', 'Legendary']] = ['Test 1', 'Test 2']
df


# # Aggregate Statistics (Groupby)

# In[106]:


df = pd.read_csv('modified.csv')
df.groupby(['Type 1']).mean()


# In[108]:


df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)


# In[109]:


df.groupby(['Type 1']).count()


# In[111]:


df = pd.read_csv('modified.csv')
df['count'] = 1
df.groupby(['Type 1']).count()['count']


# In[112]:


df.groupby(['Type 1', 'Type 2']).count()['count']


# # Working with large amount of Data

# In[113]:


for df in  pd.read_csv('modified.csv', chunksize=5):
    print("CHUNK DF")
    print(df)
    


# In[6]:


new_df = pd.DataFrame(columns=df.columns)


for df in  pd.read_csv('modified.csv', chunksize=5):    
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])


# In[ ]:





# In[ ]:




