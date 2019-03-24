#
# <==================== import libraries =================>
#

#
# General
#
import requests # connecting to websites by post and put ..
import json
from datetime import datetime
#
# local files
#
import functions.connect_firebase as cf # connecting to the online database

#
# Scraping
#
from bs4 import BeautifulSoup

#
# progress bar
#
from ipywidgets      import FloatProgress
from IPython.display import display

#
# Constants
#
with open('data/constants.json', encoding='utf-8') as data_file:
    cnsts = json.loads(data_file.read())
# <================== Finished importing ==================>

#
# Connect to firebase
#
config = cnsts['config']

try:
    database, storage = cf.connect_firebase(config)
except Exception as ex:
        print('# Exception when trying to connect to Firebase!')
        print(str(ex))
        
# <================== Connected to firebase ===============>

def parse(url, headers,title_format = ' ', body_format = ' '):    
    """
        This module will parse each website page by taking the text\
        by taking the text in it, and the title.
    """
    
    # initialize
    title  = " "
    body   = " "
    result = {
        'title':title,
        'body' :body
    }
    
    
    # try to connect
    try:
        r = requests.get(url, headers=headers)
        
        # if connected successfully
        if r.status_code == 200:
            
            # take title and body
            soup          = BeautifulSoup(r.text, 'lxml')
            title_section = soup.find(title_format)
            body_section  = soup.select(body_format)
            
            # check results
            if title_section:
                title = title_section.string
            if body_section:
                # append each body section
                for body_index in body_section:
                    body       += body_index.text.strip()
            #
            result = {
                'title' : title, 
                'body'  : body
            }
    except Exception as ex:
        print('# Exception while parsing!')
        print(str(ex))
    finally:
        return result
    

def store_info(dictionary,headers, limit = 3):   
    """
        Takes the first page of a newspaper, goes into all of its content.
        Uses the parse method to take the extra information.
    """
    

    #logging.basicConfig(level=logging.ERROR)
    
    # take the first page
    r   = requests.get(dictionary['url'], headers=headers)
    
    # if valid
    if r.status_code == 200:
        
        # initialize
        links = []
        html  = r.text
        
        # read the website
        soup  = BeautifulSoup(html, 'lxml')
        
        # some pages have multiple ways of calling each news
        for each in dictionary['links']:
            links += soup.select(each)
            
        # progress bar
        max_count = len(links)
        f = FloatProgress(min=0, max=max_count) # instantiate the bar
        display(f) # display the bar
        
        if len(links) > 0:
            for link in links:
                f.value += 1 # signal to increment the progress bar
                #sleep(1)
                try:
                    if link['href'].startswith('/'):
                        linking = dictionary['url']+link['href'][1:]
                    else:
                        linking = link['href']
                    result = parse(linking, headers,dictionary['title'],dictionary['body'])
                    #print(result['body'])
                    if result['body'] != ' ' and result['title'] != ' ':
                        database.child(dictionary['name']).child(datetime.today().\
                           strftime('%Y-%m-%d')).child(result['title']).set(result['body'])
                except Exception as ex:
                    None
                    #print("Showing exceptions while reading the links provided to the news.")
                    #print()                    #print("Link was not read properly because it is of the format: {0}"\
                    #and has created an exception of type : {1}.".format(link,str(ex))) 