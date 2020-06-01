#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Monday Special : Web Scrapping | #DS360withAkanksha 


# In[1]:


pip install beautifulsoup4


# In[2]:


pip install requests


# In[3]:


pip install pandas


# In[25]:


import pandas as pd


# In[2]:


import requests

from bs4 import BeautifulSoup


# In[10]:


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.95222000000007&lon=-75.16217999999998#.XtVRmTpKhEY')
soup = BeautifulSoup(page.content, 'html.parser')   
                 


# In[11]:


print(soup)
  


# In[12]:


week = soup.find(id='seven-day-forecast-body')


# In[13]:


print(week)


# In[14]:


items = week.find_all(class_='tombstone-container')


# In[16]:


print(items[0])


# In[18]:


print(items[0].find(class_ = 'period-name').get_text())


# In[19]:


print(items[0].find(class_ = 'short-desc').get_text())


# In[20]:


print(items[0].find(class_ = 'temp').get_text())


# In[22]:


period_names = [item.find(class_ = 'period-name').get_text() for item in items]
print(period_names)


# In[24]:


period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures= [item.find(class_ = 'temp').get_text() for item in items]


print(period_names)
print(short_descriptions)
print(temperatures)


# In[26]:


weather_details = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures
    })

print(weather_details)


# In[28]:


weather_details.to_csv('weather_forecast.csv')


# In[ ]:




