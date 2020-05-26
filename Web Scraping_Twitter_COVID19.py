# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Monday Special|Web Scraping | #DS360withAkanksha
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020,1,1)
end_date = dt.date(2020,5,25)

limit = 100
lang = 'english'


tweets = query_tweets("covid19", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
df = pd.DataFrame(t.__dict__ for t in tweets)

#Saving dataframe as csv file

df.to_csv (r'C:\Users\akank\Desktop\export_dataframe.csv', index = False, header=True)

print (df)