#!/usr/bin/env python
# coding: utf-8

# # Uber Data Analysis
# ## Uber Pickups Numbers in New York City 
# ## Xiaodan Chen 
# ## 2021-10-14

# ### Importing the Essential Packages

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Reading Data

# In[2]:


uber_df = pd.read_csv('/Users/dani/Desktop/Python_Project/Uber/uber_dataset.csv')


# In[3]:


uber_df.tail(5)


# ### Data Structure

# This dataset contains more than 4.5 millions observations and 13 columns.

# In[4]:


uber_df.shape


# In[5]:


uber_df.info()


# ### Checking any Missing Values

# In[6]:


uber_df.isnull().values.any()


# ### Number of Trips in a Day

# The number of trips that the passengers made in a day, showing the number of passengers fares throughout the day. 

# In[6]:


hour = uber_df['hour']
hour_df = hour.value_counts()
hour_df


# The number of trips are higher in the evening around 5:00 and 6:00 PM. 

# In[4]:


fig, ax = plt.subplots()
sns.countplot(data=uber_df, x = 'hour')
ax.set(title = 'Number of Trips in a Day')


# ### Number of Trips during Every Day of the Month

# The result shows the 30th of the month had the higest trips in the year. 

# In[8]:


day = uber_df['day']
day_df = day.value_counts()
day_df


# In[5]:


fig, ax = plt.subplots()
sns.countplot(data=uber_df, x = 'day')
ax.set(title = 'Number of Trips During Every day of the Month')


# ### Number of Trips on Every Day of the Week

# In[10]:


week = uber_df['dayofweek']
week_df = week.value_counts()
week_df


# In[13]:


fig, ax = plt.subplots()
sns.countplot(data=uber_df, x = 'dayofweek')
ax.set(title = 'Number of Trips on Every Day of the Week')


# In[12]:


month = uber_df['month']
month_df = month.value_counts()
month_df


# ### Number of Trips Taking Place during Months in a Year

# In[14]:


fig, ax = plt.subplots()
sns.countplot(data = uber_df, x = 'month')
ax.set(title = 'Number of Trips During Months in a Year')


# In[23]:


week_month = uber_df[['month', 'dayofweek', 'Date.Time']]
week_month = week_month.groupby(['month', 'dayofweek']).agg('count')
week_month


# ### Number of Trips on Day of Week during Months

# In[27]:


fig, ax = plt.subplots()
sns.countplot(x='month', data = uber_df, hue = 'dayofweek')
ax.set(title = 'Number of Trips on Day of Week during Months')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[24]:


week_month = week_month.pivot_table(index='month', columns='dayofweek', values='Date.Time')
week_month


# In[40]:


week_month.plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# ### Number of Trips on Day during Months

# In[46]:


fig, ax = plt.subplots()
sns.countplot(x='month', data = uber_df, hue = 'day')
ax.set(title = 'Number of Trips on Day during Months')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., ncol=4)


# In[42]:


day_mon = uber_df[['month', 'day', 'Date.Time']]
day_mon = day_mon.groupby(['month', 'day']).agg('count')
day_month = day_mon.pivot_table(index='day', columns='month', values='Date.Time')
mon_day = day_mon.pivot_table(index='month', columns='day', values='Date.Time')
mon_day


# In[43]:


day_month.plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# ### Number of Trips in Hour during Months

# In[49]:


fig, ax = plt.subplots()
sns.countplot(x='month', data = uber_df, hue = 'hour')
ax.set(title = 'Number of Trips in Hour during Months')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., ncol=2)


# In[36]:


hour_mon = uber_df[['month', 'hour', 'Date.Time']]
hour_mon = hour_mon.groupby(['month', 'hour']).agg('count')
hour_month = hour_mon.pivot_table(index='hour', columns='month', values='Date.Time')
month_hour = hour_mon.pivot_table(index='month', columns='hour', values='Date.Time')
month_hour


# In[44]:


hour_month.plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# ### Heatmap Visualization of Hour, Day, Day of Week and Month

# Heatmap by Hour and Day.

# In[32]:


hour_day = uber_df[['day', 'hour', 'Date.Time']]
hour_day = hour_day.groupby(['day', 'hour']).agg('count')
hour_day = hour_day.pivot_table(index='hour', columns='day', values='Date.Time')

fig, ax = plt.subplots()
sns.heatmap(hour_day)
ax.set(title = 'Heatmap by Hour and Day')


# Heatmap by Month and Day.

# In[33]:


month_day = uber_df[['day', 'month', 'Date.Time']]
month_day = month_day.groupby(['day', 'month']).agg('count')
month_day = month_day.pivot_table(index='month', columns='day', values='Date.Time')

fig, ax = plt.subplots()
sns.heatmap(month_day)
ax.set(title = 'Heatmap by Month and Day')


# Heatmap by Month and Day of the Week.

# In[34]:


fig, ax = plt.subplots()
sns.heatmap(week_month)
ax.set(title = 'Heatmap by Month and Day of the Week')


# Heatmap by Hour and Month.

# In[37]:


fig, ax = plt.subplots()
sns.heatmap(hour_month)
ax.set(title = 'Heatmap by Hour and Month')

