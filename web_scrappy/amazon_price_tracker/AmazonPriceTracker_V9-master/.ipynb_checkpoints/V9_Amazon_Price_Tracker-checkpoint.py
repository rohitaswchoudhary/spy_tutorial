#!/usr/bin/env python
# coding: utf-8

# # Amazon Price Tracker

# **Data Science with Raghav**

# ### Price Tracking on Amazon

# This notebook demonstrates how we can create an automated python script to autmatically alert us whenever there is a price change in the item we are interested in. In addition to alerts this script will also store the price history in a pandas DataFrame for further analysis.

# For this we will need to scrape data from Amazon using BeautifulSoup library.

# **Dependencies**

# In[1]:


from bs4 import BeautifulSoup
import requests
import random
import time
import pandas as pd

import os
from os import path

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib, ssl
import sys


# **Read Target URL from a file**

# In[2]:


target_URL = []
target_name = []
file_name = 'target_products.txt'
def get_target_products_from_file(file_name):
    global target_URL
    global target_name
    target_df = pd.read_csv(file_name)
    print(f'Total products to be scraped: {target_df.shape[0]}')
    target_URL.extend(target_df['URL'].to_list())
    target_name.extend(target_df['Name'].to_list())


# In[3]:


get_target_products_from_file('target_products.txt')


# **Browser Header**

# In[4]:


headers = {
        'authority': 'www.amazon.com',
        'user-agent': 'Chrome/86.0.4240.198',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
     


# In[5]:


header = {'authority': 'www.amazon.com',
'method': 'GET',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'dnt': '1',
'downlink': '10',
'ect': '4g',
'rtt': '50',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': 1,
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


# **Get URL HTML**

# In[6]:


def get_html(url):
    global headers
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        return False


# **Get HTML Soup**

# In[7]:


def get_html_soup(content):
    soup = BeautifulSoup(content,"lxml")
    return soup


# **Get Price**

# In[8]:


def get_value_by_id(soup,element_id):
    try:
        value = soup.select(element_id)[0].get_text()
        return value
    except:
        #print(f'Element {element_id} not found')
        pass
    return False

def get_value_by_tag(soup,tag):
    try:
        value = soup.findAll(tag)
        if len(value) >0:
            value = value[0].get_text()
            return value
    except:
        pass
    return False

def get_price(soup):
    element_ids = ['#priceblock_ourprice','#priceblock_dealprice']
    for element_id in element_ids:
        price = get_value_by_id(soup,element_id)
        if price:
            return price
    return 'Not Found'


# **Get Title**

# In[9]:


def get_title(soup):
    element_ids = ['#title','#productTitle']
#    tags = ['title']
    for element_id in element_ids:
        title = get_value_by_id(soup,element_id)
        if title:
            title = title.strip("\n")
            return title
#     for tag in tags:
#         title = get_value_by_tag(soup,tag)
#         if title:
#             return title
    return 'Not Found'


# In[10]:


# #Test
# content = get_html('https://www.amazon.com/Bose-SoundLink-Micro-Bluetooth-speaker/dp/B0748N1BZD')
# #content = get_html('https://www.amazon.com/Kindle-Now-with-Built-in-Front-Light/dp/B07978J597')

# if content:
#     soup = get_html_soup(content)
#     title = soup.select('#title')
#     print(title)
#     title = get_title(soup)
#     print(title)
# #print(content)
# #ids = [tag['id'] for tag in soup.select('div[id]')]

# #soup.select('priceblock_ourprice')

# soup.find(id='priceblock_ourprice')
# #print(soup.find("div", {"id": "desktop_unifiedPrice"}))

# file = open("MyFile.txt", "w") 
# file.write(str(content))
# file.close()


# **Get Current Date Time**

# In[11]:


import datetime
def get_current_datetime():
    now = datetime.datetime.now()
    d1 = now.strftime("%Y%m%d_%H%M%S")
    #print(d1)
    return d1


# **Data Frame to maintain Price History**

# In[12]:


if path.exists('price_history.csv'):
    print('Loading Existing Price History')
    price_history_df = pd.read_csv('price_history.csv')
    print(f'Price History initialize with {price_history_df.shape[0]} records.')
else:
    price_history_df = pd.DataFrame(columns=['crawled_datetime','url','product_name','title','price','price_changed_flag'])


# In[13]:


price_history_df.tail()


# **Add row to the DataFrame**

# In[14]:


def append_row_to_price_history_df(row):
    global price_history_df
    df_length = len(price_history_df) 
    price_history_df.loc[df_length] = row


# **Check if price has changed since last run**

# In[15]:


def has_price_changed(row):
    product_name = row[2]
#     print(product_name)
    last_price = get_last_price(product_name)
#     print(last_price)
#     print(row)
#     print(row[4])
    if last_price =='Not Found':
        return False
    if last_price != row[4]:
        print('Price Changed Detected')
        return True
    else:
        return False


# **Get Previous Run's price**

# In[16]:


def get_last_price(product_name):
    global price_history_df
    most_recent_row = price_history_df.loc[price_history_df['product_name']==product_name]
    if len(most_recent_row) >0 and most_recent_row.iloc[-1]['price'] != 'Not Found' :
        return int(most_recent_row.iloc[-1]['price'])
    else:
        return 'Not Found'


# **Convert Price to Number**

# In[17]:


def get_price_in_num(price):
    if len(price) >0 and price[0]=='$':
        return int(float(price[1:]))
    else:
        return 'Not Found'


# **Function to wait for random seconds before hitting Amazon.com**

# In[18]:


def random_wait():
    sleep_times= [3,5,8,10]
    sleep_time = random.choice(sleep_times)
    print(f'Sleeping for {sleep_time} seconds before hitting Amazon again ')
    time.sleep(sleep_time)


# **Main Loop**

# In[19]:


last_run_index = price_history_df.shape[0]
for index,url in enumerate(target_URL):
    print(f'Getting prices for {target_name[index]}')
    scraped_date_time = get_current_datetime()
    content = get_html(url)
    if content:
        soup = get_html_soup(content)
        price = get_price_in_num(get_price(soup))
        title = get_title(soup)
        #print(f'{target_name[index]} - {title} price is {price}')
    else:
        print(f'Invalid URL - {url}')
        price = 'Not Found'
        title = 'Not Found'
    row = [scraped_date_time,url,target_name[index],title,price]
    if has_price_changed(row):
        price_changed_flag = 1
    else:
        price_changed_flag = 0
    row.append(price_changed_flag)
    append_row_to_price_history_df(row)
    if index < len(target_URL) -1:
        random_wait()
    else:
        print('Done.')


# In[20]:


price_history_df.tail(10)


# **Detect Changes and Send Email**

# In[21]:



def get_pwd():
    with open('pwd.txt','r') as f:
        return f.readline()

    
    
def prepare_html_msg(df):
    msg = MIMEMultipart()
    msg['Subject'] = "Price Change Detected"
    msg['From'] = 'raagabot@gmail.com'
    html = """            <html>
            <head></head>
            <body>
            {0}
            </body>
            </html>
            """.format(df.to_html())
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    return msg

def send_email(msg):
    recipients = ['raghav.atal@gmail.com'] 
    emaillist = [elem.strip().split(',') for elem in recipients]
    sender = 'raagabot@gmail.com'
    # Create secure connection with server and send email
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, get_pwd())
        server.sendmail(
            sender, emaillist, msg.as_string()
        )
        
def check_and_send_email():
    global price_history_df
    df = price_history_df.iloc[last_run_index:]
    changed_df = df[df['price_changed_flag']==1]
    if changed_df.shape[0] >0:
        msg = prepare_html_msg(changed_df)
        send_email(msg)
        print('Emal Sent.')
    else:
        print('No Price Change Detected')


# In[22]:


check_and_send_email()


# **Save price history to disk**

# In[23]:


price_history_df.to_csv('price_history.csv',index=False)


# **Save notebook as python script**

# In[25]:


#get_ipython().system('jupyter nbconvert --to script V9_Amazon_Price_Tracker.ipynb')


# In[ ]:




