# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
from nltk.corpus   import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string
import nltk
import numpy as np

def clean_text(text):
    """
        Remove the words which do not add meaning to the text.
    """

    stopwords_set  = set(stopwords.words("english"))

    
    # remove small words
    text = [e.lower() for e in text.split() if len(e) >= 3]
    
    # remove remaining tokens that are not alphabetic
    text = [word for word in text if word.isalpha()]


    # remove hashtags and the like
    text_cleaned  = [word for word in text
        if 'http' not in word
        and not word.startswith('@')
        and not word.startswith('#')
        and word != 'RT']

    # remove stopwords
    text_without_stopwords = [word for word in text_cleaned if not word in stopwords_set]

    # stemming of words
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in text_without_stopwords]
    #text = " ".join(stemmed)
    return stemmed

# not useful for now
def find_features(text):
    """
        Measure frequency of a word in a list and return the features.
    """
    
    wlist = clean_text(text)
    wlist = nltk.FreqDist(wlist)
    features = wlist.keys()
    return features
    