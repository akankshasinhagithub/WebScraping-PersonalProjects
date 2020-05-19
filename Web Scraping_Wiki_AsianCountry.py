#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the library to query a website
import requests
#specify the url
wiki_link="https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link=requests.get(wiki_link).text


# In[2]:


print(link)


# In[3]:


#importing the 'BeautifulSoup' library
from bs4 import BeautifulSoup
soup = BeautifulSoup(link, 'lxml')
print(soup)


# In[5]:


print(soup.prettify())


# In[6]:


soup.title


# In[7]:


soup.title.string


# In[8]:


soup.a


# In[9]:


soup.find_all("a")


# In[10]:


all_link=soup.find_all("a")
for link in all_link:
    print(link.get("href"))


# In[11]:


#To identify all contents within the table
all_tables=soup.find_all('table')
print(all_tables)


# In[12]:


#to identify the right table
right_table=soup.find('table', class_='wikitable sortable')
right_table


# In[13]:


#To get the correct 'a' tags
table_links = right_table.findAll('a')
table_links


# In[18]:


#To get the country names
country = []
for links in table_links:
    country.append(links.get('title'))
    print(country)
    


# In[19]:


#Importing Pandas library
import pandas as pd
df = pd.DataFrame()
df['Country']=country
df


# In[25]:



pip install openpyxl


# In[29]:


df.to_excel(r'C:\Users\akank\Desktop\export_Asian Country List.xlsx', index = False)


# In[ ]:





# In[ ]:




