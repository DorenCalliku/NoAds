## NoAds
----------------

1. Read from newspapers only the useful information, without advertisements(No-Advertisements).
    * Scrape with bs4. 
    
2. Measure Sentiment of the information.
    * Use Vader for English language. 
    * Use sklearn's vectorized work for the Albanian version. (todo)
        * Make use of the stemming-word method. 
        
3. Collect news articles for creating a classifier. (here)
    * Should be both in English and Albanian.
    * Classifier should have heuristic(logical) classes.
    * Can be Supervised at first, and unsupervised next. 
    
4. Create a text classifier for news type.
    * Understand different classifiers, pick one according to your knowledge.
    * Check its accuracy.
    * Check the others and analyse your choice.
    
5. Recommend which news to read with an email. 
    * Create accounts
        * Use Auth of Firebase
    * Recommendation system based on shown user-preference (cold-start).
    * Add history based recommendations to the user. 
        * Content based recommendations (usage of sparse matrix of data)
        * Collaborative filtering based on customer segmentation language and locality based.
    

### Used:
------
* Python (Webscraping, Sentiment Analysis, Text classifier)
* Firebase (Server, Database)

### Aim: 
-----
1. Learn Natural Language Processing.
2. Understand Sentiment Analysis.
3. Create a classifier for the Albanian language. 
4. Be able to recommend Albanian news, not just by checking a bag of words.

Disclaimer: 
-----
This is not a product, it is just a personal project for learning the technology and its usage. In the end I expect personal usage.


<hr> <hr>

## Shqip
-----

1. Lexoni nga gazetat vetëm informacionin e dobishëm, pa reklama (nga ku vjen emri NoAds).
    * Lexo faqen me ane te bs4.
    
2. Matje e sasise se ndjenjave te informacionit.
    * Përdor Vader për gjuhën angleze.
    * Përdor vektorizimin të [sklearn](https://scikit-learn.org/stable/index.html) për versionin shqip. (për të bërë)
        * Bëj përdorimin e metodës stemming-word.
        
3. Mblidh artikuj të lajmeve për krijimin e një klasifikuesi. (Këtu eshte puna per tani.)
    * Duhet të jenë të dyja, edhe në anglisht, dhe shqip.
    * Klasifikuesi duhet të ketë klasa logjike.
    * Mund të mbikëqyret në fillim(supervised) dhe pa mbikëqyrje tjetër(unsupervised).
    
4. Krijo një klasifikues teksti për llojin e lajmit.
    * Kupto klasifikues të ndryshëm, zgjidh një sipas njohurive.
    * Kontrollo saktësinë e saj.
    * Kontrollo të tjerët dhe analizoni zgjedhjen tuaj.
    
5. Rekomando cilat lajme të lexoni me ane te një email.
    * Krijo llogaritë
        * Përdorni Auth of Firebase.
    * Sistemi i rekomandimit bazuar në preferencën e treguar të përdoruesit (cold-start).
    * Shto rekomandime të bazuara në histori tek përdoruesi.
        * Rekomandimet e bazuara në përmbajtje (përdorimi i matricës së rrallë të të dhënave)
        * Filtrim bashkëpunues bazuar në gjuhën dhe lokalitetin e segmentimit të konsumatorëve.
    

### Të përdorura:
------
* Python (Webscraping, Analiza Sentiment, klasifikues teksti)
* Firebase (Server, Baza e të dhënave)

### Qëllimi:
-----
1. Mësoni Përpunimin e Gjuhës Natyrore.
2. Kuptoni Analizën e Sentimentit.
3. Krijo një klasifikues për gjuhën shqipe.
4. Të jetë në gjendje të rekomandojë lajmin shqiptar, jo vetëm duke kontrolluar një thes me fjalë.

### Disclaimer:
-----
Ky nuk është një produkt, është vetëm një projekt personal për të mësuar teknologjinë dhe përdorimin e saj. Në fund unë pres përdorimin personal meqe zgjedhjet e ketij sistemi te dhenash do te perdoren nga une.
