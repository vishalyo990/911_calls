
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

import numpy as np


# In[4]:

import matplotlib.pyplot as plt


# In[6]:

import seaborn as sns


# In[7]:

get_ipython().magic(u'matplotlib inline')


# In[8]:

df = pd.read_csv("C://Users//user//Desktop//911.csv")


# In[9]:

df.info()


# In[10]:

df.head()


# In[11]:

df['zip'].value_counts().head(5)


# In[12]:

df['twp'].value_counts().head(5)


# In[14]:

df['title'].nunique()


# In[18]:

df['reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[20]:

df['reason'].head(4
                 )


# In[21]:

df['reason'].value_counts()


# In[82]:

sns.countplot(x = 'reason', data = df)


# In[30]:

type(df['timeStamp'].iloc[0])


# In[29]:

df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[31]:

df['timeStamp'].iloc[0]


# In[32]:

df['Hour'] = df['timeStamp'].apply(lambda time:time.hour)


# In[33]:

df['Hour'].head(5)


# In[48]:

df['month'] = df['timeStamp'].apply(lambda time:time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time:time.dayofweek)


# In[49]:

df.head(3)


# In[50]:

dmap = {0:'mon', 1:'tue',2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}


# In[51]:

df['Day of Week'] = df['Day of Week'].map(dmap)


# In[55]:

df['Day of Week'].nunique()


# In[58]:

sns.countplot(data = df, x = 'Day of Week', hue = 'reason', palette = 'viridis')
plt.legend(bbox_to_anchor = (1.05,1), loc = 2, borderaxespad = 0)


# In[59]:

sns.countplot(data = df, x = 'month', hue = 'reason', palette = 'viridis')
plt.legend(bbox_to_anchor = (1.05,1), loc = 2, borderaxespad = 0)


# In[62]:

df['date'] = df['timeStamp'].apply(lambda t:t.date())


# In[63]:

df.head(3
       )


# In[67]:

df.groupby('date').count()['lat'].plot()
plt.tight_layout()


# In[69]:

df[df['reason']=='Traffic'].groupby('date').count()['lat'].plot()
plt.tight_layout()
plt.title('Traffic')


# In[70]:

df[df['reason']=='EMS'].groupby('date').count()['lat'].plot()
plt.tight_layout()
plt.title('EMS')


# In[71]:

df[df['reason']=='Fire'].groupby('date').count()['lat'].plot()
plt.tight_layout()
plt.title('Fire')


# In[86]:

dayHour = df.groupby(by = ['Day of Week', 'Hour']).count()['reason'].unstack()


# In[78]:

sns.heatmap(dayHour, cmap = 'viridis')


# In[81]:

sns.clustermap(dayHour, cmap = 'viridis')


# In[88]:

dayMonth = df.groupby(by = ['Day of Week', 'month']).count()['reason'].unstack()


# In[89]:

dayMonth


# In[92]:

sns.heatmap(dayMonth, cmap = 'viridis')


# In[94]:

sns.clustermap(dayMonth, cmap = 'coolwarm')


# In[ ]:



