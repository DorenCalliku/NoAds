# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:11:25 2018

@author: owner
@template: webscraping tables
"""

# web scraping from the website for data

#
# Import the basic libraries
#
import requests
import csv,re
import pandas as pd
from bs4 import BeautifulSoup

#
# get the content, and then the table
#
url         = 'https://en.wikipedia.org/wiki/Demographics_of_Albania'
headers     = {'User-Agent':'Mozilla/5.0'}
response    = requests.get(url,headers = headers) # headers expects dictionary, as given
# response.status_code    # should be 200
soup        = BeautifulSoup(response.content, 'html.parser') # 'lxml' if wikipedia
stat_table  = soup.find_all('table', class_ ='sortable')
stat_table  = stat_table[2] # take the first table.

len(stat_table)
print(stat_table)

#
# take all of the information and put it in an csv file
#
with open('demographics_of_albania.csv', 'w' ) as f: 
    csv_writer  = csv.writer(f)
    row_index   = 0
    cell_index  = 0
    csv_content = []
    dummy = ""
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
#            dummy = ''.join(re.findall(r"[-+]?\d*\.\d+|\d+",cell.text))
#            dummy = dummy.encode("utf-8")
            csv_content.append(cell.text)
            cell_index = cell_index + 1 
        csv_writer.writerow(csv_content)
        row_index = row_index + 1
        cell_index = 0
        csv_content = []
 