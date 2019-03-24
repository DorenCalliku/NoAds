# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
from nltk.corpus import stopwords
from wordcloud   import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


def draw_wordcloud(data, color = 'black'):
    """
        Visualize groups of words.
    """
    
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()