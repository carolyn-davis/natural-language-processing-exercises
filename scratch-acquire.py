#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:57:06 2021

@author: carolyndavis
"""

# =============================================================================
# Data Acquisition with Web Scraping Exercises:
# =============================================================================
# =============================================================================
# Imports
# =============================================================================
import requests
from bs4 import BeautifulSoup 
import pandas as pd

#homepage website for Codeup containing the blog page
#now we can use the root variable for other things if needed 
root = 'https://codeup.com/'

#now
website = f'{root}/blog'

headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent

#to get html content 
result = requests.get(website, headers=headers)

#get the html txt content
content = result.text

#get the soup
soup = BeautifulSoup(content, 'lxml')

#makes html code appear nicer
print(soup.prettify())




# =============================================================================
# 1.) Codeup's Blog Articles'
# Visit Codeup's Blog and record the urls for at least 5 distinct blog posts. For
#  each post, you should scrape at least the post's title and content.
# =============================================================================

#first make the request 
# =============================================================================
# Import the get() function from the requests module, BeautifulSoup from bs4, and pandas.
# =============================================================================

box = soup.find('article', {'id'='main-content'})

links = []

for link in box.find_all('li', href=True):
    links.append(link['href'])

print(links)
