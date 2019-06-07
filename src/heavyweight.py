# General
import requests # connecting to websites by post and put ..
import json
from datetime import datetime
from bs4 import BeautifulSoup
from ipywidgets      import FloatProgress # progress bar
from IPython.display import display

# local files
import src.database.functionalities as db_func # connecting to the online database

#<======================= Getting info ==================================>
def parse(url, headers,title_format = ' ', body_format = ' '):    
    """ This module will parse each website page by taking the text\
        by taking the text in it, and the title. """
    
    # initialize
    title  = " "
    body   = " "
    result = { 'title':title, 'body' :body}
    try: # try to connect
        r = requests.get(url, headers=headers)
        if r.status_code == 200: # if connected successfully
            soup          = BeautifulSoup(r.text, 'lxml')  # take title and body
            title_section = soup.find(title_format)
            body_section  = soup.select(body_format)
            if title_section: # check results
                title = title_section.string
            if body_section: # append each body section
                for body_index in body_section:
                    body       += body_index.text.strip()
            result = { 'title' : title, 'body'  : body}
    except Exception as ex:
        print(ex)
    finally:
        return result
    

def store_info(dictionary,headers, limit = 3):   
    """ Takes the first page of a newspaper, goes into all of its content.
        Uses the parse method to take the extra information. """
    
    r   = requests.get(dictionary['url'], headers=headers)
    if r.status_code == 200:    # if valid
        links = []
        html  = r.text
        soup  = BeautifulSoup(html, 'lxml')# read the website
        # some pages have multiple ways of calling each news
        for each in dictionary['links']:
            links += soup.select(each)
        max_count = len(links) # progress bar
        f = FloatProgress(min=0, max=max_count) # instantiate the bar
        display(f) # display the bar
        if len(links) > 0:
            for link in links:
                f.value += 1 # signal to increment the progress bar
                try:
                    if link['href'].startswith('/'):
                        linking = dictionary['url']+link['href'][1:]
                    else:
                        linking = link['href']
                    result = parse(linking, headers,dictionary['title'],dictionary['body'])
                    if result['body'] != ' ' and result['title'] != ' ':
                        db_func.update( dictionary['name'],{result['title'] : result['body']})
                except Exception as ex:
                    print(ex)
