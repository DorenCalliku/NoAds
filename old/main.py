from   News import News
import deduplicate
import time

if __name__ == "__main__":
	print("# Entered Main Method")
	# list of dictionaries: (url, links, name, title, body) <- newspapers to be read and scraped
	information =[     {'name':'panorama_sport','url':'http://www.panorama.com.al/sport/',\
						'title':'title','body':'.article_content p','links':[".tc-desc a"] },
					   {'name':'panorama','url':'http://www.panorama.com.al/',\
						'title':'title','body':'.td-post-content p','links':['.td-block-row a'] },
					   {'name':'new_york_times','url':'https://nytimes.com',\
						'title':'title','body':'.css-1h6whtw p','links':['.story-heading a'] },
					   {'name':'mirror','url':'https://www.mirror.co.uk/',\
						'title':'title','body':'.article-body p','links':['.inner a']},
					   {'name':'sabah','url':'https://www.dailysabah.com/',\
						'title':'title','body':'.txtInWrapper p','links':['.topHeadline a']}]
	positive = "rise rose growth high increase stability ties develop mutual lead even"
	negative = "fall fell slipped dropped down impose detention beats losing up "
	start_time = time.time()
	
	print("# Starting the news.")
	news = News()
	
	for i in range( 0, len(information)):
		print("\nReading news from {0} newspaper.".format(information[i]['name']))
		news.store_info(information[i], 3)
		#news.store_info(information[3], 2)
	deduplicate(True)
	#time python yourprogram.py
	#store_info(information[4])
	time_ =  time.time()- start_time 
	print("Time taken to read the newspapers: {0}.".format( time_))
	
	
