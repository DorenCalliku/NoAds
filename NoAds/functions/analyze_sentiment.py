#
# Import needed libraries
#

from nltk.classify        import NaiveBayesClassifier
from nltk.corpus          import subjectivity
from nltk.sentiment       import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util  import *
from nltk                 import tokenize


#
# IF YOU WANT TO FORM YOUR OWN CLASSIFIER !!!!!!!!!
#
def create_vader(text):
    """
        Use nltk's algorithm for analyzing each sentence. 
        For more: http://www.nltk.org/howto/sentiment.html.
    """
    
    # take information
    n_instances = 100
    subj_docs   = [(sent, 'subj') \
        for sent in subjectivity.sents(categories='subj')[:n_instances]]
    obj_docs    = [(sent,  'obj') \
        for sent in subjectivity.sents(categories= 'obj')[:n_instances]]
    
    # split into train and test the objective and subjective documents
    train_subj_docs = subj_docs[:80]
    train_obj_docs  =  obj_docs[:80]
    test_subj_docs  = subj_docs[80:100]
    test_obj_docs   =  obj_docs[80:100]
    
    # get together train and test 
    # Remember, first subjective docs, then objective docs
    training_docs   = train_subj_docs + train_obj_docs
    testing_docs    =  test_subj_docs +  test_obj_docs
    
    # IMPORTANT NOTE : https://www.nltk.org/_modules/nltk/sentiment/sentiment_analyzer.html#SentimentAnalyzer
    # Analyzer is a tool taking a classifier and applying feature extraction. 
    # it takes a classifier as an argument
    # for more, check share link
    sentim_analyzer = SentimentAnalyzer()

    # negation marks all the words after a negation word was introduced
    # takes care of change of meaning
    all_words_neg   = sentim_analyzer.all_words(\
                [mark_negation(doc) for doc in training_docs])
    
    # extract all unigrams - the words with a certain repeating frequency
    unigram_feats   = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
    #print(unigram_feats)

    # create the functionality of extracting unigram feats to the sentim_analyzer 
    # used in apply_features
    sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
    
    # get together the sets
    training_set = sentim_analyzer.apply_features(training_docs)
    test_set     = sentim_analyzer.apply_features( testing_docs)
    
    # create the classifier
    # https://www.nltk.org/_modules/nltk/classify/naivebayes.html
    trainer      = NaiveBayesClassifier.train
    classifier   = sentim_analyzer.train(trainer, training_set)

    # Training classifier
    for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
        print('{0}: {1}'.format(key, value))
    return sentim_analyzer
#print(create_vader(' '))

def analyze_text(text):
    """
        Analyze text using nltk.
    """
    
    # initialize
    sum   = 0
    count = 0
    sentences  = []
    
    # divide into sentences for single usage
    lines_list = tokenize.sent_tokenize(text)
    sentences.extend(lines_list)
    
    # call class from nltk - trained with vader lexicon
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        ss = sid.polarity_scores(sentence)
        sum = sum + ss['compound']
        count += 1
    return sum/count
            
            
#print("Average: {0}".format(analyze_text("I am well. Be positive. Dont kill.")))