# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:27:11 2019

@author: Akhil
"""
import emoji
import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re
import contractions
stopw=stopwords.words('english')
stopw.remove('not')
happy_set = set([":)",":-)","=)",":-]",":-3",":->",":-}",":]",":3",":>",":}","=>","=)","=]",":-D",":D",":-))",":'-)"])
sad_set = set([":(",":-(","=(",":-c",":-<",":-[",":<",":[",":-||",":{",":'-(",":("])  
def process(tweet):
    #set of text emoticons that indicate happiness
    #happy_set = set([":)",":-)","=)",":-]",":-3",":->",":-}",":]",":3",":>",":}","=>","=)","=]",":-D",":D",":-))",":'-)"])
    #set of text emoticons that indicate sadness
    #sad_set = set([":(",":-(","=(",":-c",":-<",":-[",":<",":[",":-||",":{",":'-(",":("])
    #replace text emoticons with meaningful words
    for i in happy_set:
        tweet=tweet.replace(i,"happy")
    for j in sad_set:
        tweet=tweet.replace(j,"sad")
    #replacing unicode emojis with equivalent symbols
    tweet=emoji.demojize(tweet)
    #removing html special entities
    tweet=re.sub(r'\&\w*;','',tweet)
    
    #removing twitter handles
    tweet=re.sub(r'@[^\s]+','',tweet)
    
    #removing unnecessary info
    tweet=re.sub(r'\\x..','',tweet)
    
    #removing tickers
    tweet=re.sub(r'\$\w*','',tweet)
    
    #making all letters lowercase in tweet
    tweet=tweet.lower()
    
    #removing hyprlinks
    tweet=re.sub(r'(http)?(s)?:\/\/.*\/\w*','',tweet)
    
    #removing hashtags
    tweet=re.sub(r'#\w*','',tweet)
    
    #expanding words like hasn't doesn't etc.
    tweet=contractions.fix(tweet)          
    
    #tweet=re.sub(r'['+punctuation.replace('@','')+']+','',tweet)
    
    #removing words less than equal to two letters
    tweet=re.sub(r'\b\w{1,2}\b','',tweet)
    
    #removing whitespaces
    tweet=re.sub(r'\s\s+',' ',tweet)
    
    #removing empty space preceeding the tweet
    tweet=tweet.lstrip(' ')
    
    #removing characters beyond basic multilingual plane
    tweet=''.join(c for c in tweet if c<='\uFFFF')
    
    #tokenizing the tweet
    tweet=nltk.wordpunct_tokenize(tweet)
    
    #removing punctuation symbols
    tweets=[]
    for i in tweet:
        newi=re.sub(r'[^\w\s]','',i)
        if newi!='':
            tweets.append(newi)
    tweet=tweets
    
    #removing stopwords
    tweets=[]
    for i in tweet:
        if i not in stopw:
            tweets.append(i)
    tweet=tweets
    tweet=' '.join(tweet)
    
    #removing underscores due to demojizing tweets
    tweet=re.sub(r'_',' ',tweet)
    
    #removing numbers from the tweet
    tweet=re.sub(r'\d','',tweet)
    return tweet
