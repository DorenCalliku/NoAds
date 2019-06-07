# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
import matplotlib.pyplot as plt
from nltk.corpus import stopwords # filter out stop words
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string
import nltk
import numpy as np

def draw_wordcloud(data, color = 'black'):
    """Visualize groups of words."""

    from wordcloud   import WordCloud,STOPWORDS
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width =2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def count(text):
    from sklearn.feature_extraction.text import CountVectorizer

    
    vectorizer = CountVectorizer()# create the transform
    tokens = [w.lower() for w in text]  # tokenize and build vocab
    stop_words = set(stopwords.words('english'))
    words = [w for w in tokens if not w in stop_words]
    from nltk.stem.porter import PorterStemmer  # stemming of words
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in words]
    vectorizer.fit(stemmed)
    print(vectorizer.vocabulary_) # summarize
    vector = vectorizer.transform(text)
    print(vector.toarray())

# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis


def clean_text(text):
    """Remove the words which do not add meaning to the text."""

    stopwords_set  = set(stopwords.words("english"))
    text = [e.lower() for e in text.split() if len(e) >= 3] # small words
    text = [word for word in text if word.isalpha()] # alphabetic
    text_cleaned  = [word for word in text  # remove hashtags and the like
        if 'http' not in word
        and not word.startswith('@')
        and not word.startswith('#')
        and word != 'RT']
    text_without_stopwords = [word for word in text_cleaned if not word in stopwords_set]
    porter  = PorterStemmer()
    stemmed = [porter.stem(word) for word in text_without_stopwords]
    return stemmed

# not useful for now
def find_features(text):
    """Measure frequency of a word in a list and return the features."""
    
    wlist = clean_text(text)
    wlist = nltk.FreqDist(wlist)
    features = wlist.keys()
    return features
    
