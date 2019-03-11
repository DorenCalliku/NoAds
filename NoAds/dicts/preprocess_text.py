import numpy as np
def process(text):
	
	# split into words
	from nltk.tokenize import word_tokenize
	tokens = word_tokenize(str(text))

	# convert to lower case
	tokens = [w.lower() for w in tokens]

	# remove punctuation from each word
	import string
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in tokens]

	# remove remaining tokens that are not alphabetic
	words = [word for word in stripped if word.isalpha()]

	# filter out stop words
	from nltk.corpus import stopwords
	stop_words = set(stopwords.words('english'))
	words = [w for w in words if not w in stop_words]

	# stemming of words
	from nltk.stem.porter import PorterStemmer
	porter = PorterStemmer()
	stemmed = [porter.stem(word) for word in words]

	return [" ".join(stemmed)]


text = ["The quick brown fox jumped over the lazy dog. Doren."]
processed = process(text)
# create the transform
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(processed)

# encode another document
text2  = ["brown brown brown."]
vector = vectorizer.transform(process(text2))
print(np.sum(vector))