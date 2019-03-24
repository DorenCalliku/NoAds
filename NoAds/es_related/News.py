# import libraries
import json
import logging
import time
import requests
import hashlib

from elasticsearch import Elasticsearch
from pprint        import pprint
from time          import sleep
from bs4           import BeautifulSoup

# progress bar:
from ipywidgets      import FloatProgress
from IPython.display import display

from Sentiment import Sentiment_Analyzer
#from PyDictionary import PyDictionary
#from nltk         import *


class News():
	def __init__(self):
		self.analyzer = Sentiment_Analyzer()
		
	def search(self,es_object, index_name, search):
		res = es_object.search(index=index_name, body=search)
		pprint(res) 

	def create_index(self,es_object, index_name):    
		created = False
		# index settings
		settings = {
			"settings": {
				"number_of_shards":   1,
				"number_of_replicas": 0
			},
				"news": {
					"dynamic": "strict",
					"properties": {
						"title": {
							"type": "text"
						},
						"body": {
							"type": "text"
						},
						"sentiment":{
							"type": "float"
						},
					  }
					}
				}
		try:
			if not es_object.indices.exists(index_name):
				# Ignore 400 means to ignore "Index Already Exist" error.
				es_object.indices.create(index=index_name, ignore=400, body=settings)

			created = True
		except Exception as ex:
			print(str(ex))
		finally:
			return created
		
	def store_record(self,elastic_object, index_name, record):    
		is_stored = True
		try:
			outcome = elastic_object.index(index=index_name, doc_type='news', body=record)
			#print(outcome)
		except Exception as ex:
			print('Error in indexing data')
			print(str(ex))
			is_stored = False
		finally:
			return is_stored
	 
	def connect_elasticsearch(self):
		_es = None
		host = 'localhost'
		port = 9200
		_es = Elasticsearch([{'host': host, 'port': port}])
		if _es.ping():
			print('Connected to the {0} at port {1}.'.format(host,port))
		else:
			print('It could not connect to the {0} at port {1}.'.format(host,port))
		return _es

	def parse(self,url, headers,title_format = ' ', body_format = ' '):    
		rec   = {}
		title = " "
		body  = " "
		try:
			r = requests.get(url, headers=headers)
			if r.status_code == 200:
				html = r.text
				soup = BeautifulSoup(html, 'lxml')
				title_section = soup.find(title_format)
				body_section  = soup.select(body_format)
				if body_section:
					for body_index in body_section:
						body       += body_index.text.strip()
				if title_section:
					title = title_section.string
				rec = {'title': title, 'body': body }
		except Exception as ex:
			print('Exception while parsing')
			print(str(ex))
		finally:
			return json.dumps(rec)

	def store_info(self,dictionary, limit = 3):    
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36',
			'Pragma': 'no-cache'
		}
		logging.basicConfig(level=logging.ERROR)
		r   = requests.get(dictionary['url'], headers=headers)
		if r.status_code == 200:
			links = []
			html  = r.text
			soup  = BeautifulSoup(html, 'lxml')
			# some pages have multiple ways of calling each news
			for each in dictionary['links']:
				links += soup.select(each)
			# progress bar
			max_count = len(links)
			f = FloatProgress(min=0, max=max_count) # instantiate the bar
			display(f) # display the bar
			if len(links) > 0:
				es = self.connect_elasticsearch()
				exception = False
				for link in links:
					f.value += 1 # signal to increment the progress bar
					#sleep(1)
					try:
						if link['href'].startswith('/'):
							linking = dictionary['url']+link['href'][1:]
						else:
							linking = link['href']
						result = self.parse(linking, headers,dictionary['title'],dictionary['body'])
					except Exception as ex: 
						if exception == False:
							#print("Showing exceptions while reading the links provided to the news.")
							print()
							exception = True
						#print("Link was not read properly because it is of the format: {0}"\
						#	  " and has created an exception of type : {1}.".format(link,str(ex)))
					else:
						if es is not None:
							try:
								body_text = json.loads(result)['body']
							except Exception as ex:
								print("\n")
							else:
								sentiment = self.analyzer.analyze(json.loads(result)['body'])
								if sentiment < (-limit) or sentiment > limit:
									out = self.store_record(es, dictionary['name'], result)

									
