from sklearn.feature_extraction.text import CountVectorizer

def count(text):

    # create the transform
    vectorizer = CountVectorizer()

    # tokenize and build vocab
    tokens = [w.lower() for w in text]

    # filter out stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in tokens if not w in stop_words]


    # stemming of words
    from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in words]
    #for i in stemmed:
    #    print(i)
    vectorizer.fit(stemmed)
    # summarize
    print(vectorizer.vocabulary_)
    # encode document
    vector = vectorizer.transform(text)
    # summarize encoded vector
    #print(vector.shape)
    #print(type(vector))
    print(vector.toarray())
    
text = ["The quick brown fox jumped over the lazy dog."]
count(text)