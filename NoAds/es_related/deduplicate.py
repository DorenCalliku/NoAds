#!/usr/local/bin/python3
import hashlib
from elasticsearch import Elasticsearch
#  https://alexmarquardt.com/2018/07/23/deduplicating-documents-in-elasticsearch/
#------------------------------------------------------------------------------------------------------------

"""                 
es = connect_elasticsearch()
if es is not None:
	# search_object = {'query': {'match': {'calories': '102'}}}
	# search_object = {'_source': ['title'], 'query': {'match': {'calories': '102'}}}
	search_object = { "query": { "match_all" : {}}}
	#{'_source': ['title'], 'query': {'match_all':{}}}
	#search(es, 'sabah', json.dumps(search_object))
"""


def deduplicate(value = True, index = 'sabah',doc_type = 'news', key = 'title'):
	
	print("Entered")

	#from elasticsearch import Elasticsearch
	es = Elasticsearch(["localhost:9200"])
	dict_of_duplicate_docs = {}
	# The following line defines the fields that will be
	# used to determine if a document is a duplicate
	keys_to_include_in_hash = ['title']
	
	# Process documents returned by the current search/scroll
	def populate_dict_of_duplicate_docs(hits,key):
		print("Entered in method")
		for item in hits:
			combined_key = ""
			# mykey in keys_to_include_in_hash:
			combined_key += str(item['_source'].get(key,None))

			_id = item["_id"]

			hashval = hashlib.md5(combined_key.encode('utf-8')).digest()

			# If the hashval is new, then we will create a new key
			# in the dict_of_duplicate_docs, which will be
			# assigned a value of an empty array.
			# We then immediately push the _id onto the array.
			# If hashval already exists, then
			# we will just push the new _id onto the existing array
			dict_of_duplicate_docs.setdefault(hashval, []).append(_id)
	

	# Loop over all documents in the index, and populate the
	# dict_of_duplicate_docs data structure.
	def scroll_over_all_docs(index, key):
		data = es.search(index=index, scroll='1m',  body={"query": {"match_all": {}}})

		# Get the scroll ID
		sid = data['_scroll_id']
		scroll_size = len(data['hits']['hits'])

		# Before scroll, process current batch of hits
		populate_dict_of_duplicate_docs(data['hits']['hits'],key)

		while scroll_size > 0:
			data = es.scroll(scroll_id=sid, scroll='2m')

			# Process current batch of hits
			populate_dict_of_duplicate_docs(data['hits']['hits'],key)

			# Update the scroll ID
			sid = data['_scroll_id']

			# Get the number of results that returned in the last scroll
			scroll_size = len(data['hits']['hits'])

	
	def loop_over_hashes_and_remove_duplicates(index,doc_type):
		# Search through the hash of doc values to see if any
		# duplicate hashes have been found
		print(dict_of_duplicate_docs)

		for hashval, array_of_ids in dict_of_duplicate_docs.items():
			if len(array_of_ids) > 1:
				for each in range(1,len(array_of_ids)):
					es.delete(index=index,doc_type = doc_type, id = array_of_ids[each],ignore=[400, 404])
	key = ""
	scroll_over_all_docs(index,key)
	loop_over_hashes_and_remove_duplicates(index,doc_type)

#------------------------------------------------------------------------------------------------------------
deduplicate()
