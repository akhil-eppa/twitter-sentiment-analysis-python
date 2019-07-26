# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:27:02 2019

@author: Akhil
"""

import pickle
import pandas as pd
import csv
import time
import tweetcollect
#print("TWITTER SENTIMENT ANALYSIS")
#print("------- --------- --------\n")

#Twitter handle for loading tweets
#handle=input("Enter the twitter hashtag for loading tweets \n(Eg: #IndianArmy, #20YearsOfKargilWar etc.) \nEnter here==>")
#api=tweepy.API(auth,wait_on_rate_limit=True)
#opening csv file to write all the tweets into

#Function to collect and then process loaded tweets
#print("Fetching of required tweets has begun. Please wait.....")
#Model is loaded using pickle module
#Time is saved as computation is not required each time
def calculate(handle):
    with open('model.pkl', 'rb') as f:
        vct,clf = pickle.load(f)
    tweetcollect.start_collection(handle)
    df=open("trial4.csv","rt")
    reader2=csv.reader(df,delimiter=",")
    test=[]
    for row in reader2:
        if row[0]!='':
            test.append(row[0])
    #print("Fetching and preprocessing of tweets has been completed!")
    #print(len(test))
    #test_vectors = vectorizer.transform(test)
    #predicted=classifier.predict(test_vectors)
    #x=predicted.tolist()
    #print(x.count('4'))
    
    #with open('model.pkl', 'rb') as f:
    #    vct,clf = pickle.load(f)
    
    #Vectorizing processed tweets
    #print("Vectorizing downloaded tweets....")
    test_vectors2=vct.transform(test)
    #Making predictions with the model we loaded
    #print("Analysing downloaded tweets...\n")
    pred2=clf.predict(test_vectors2)
    #Converting numpy array to a list
    x=pred2.tolist()
    #Count of positive comments
    pos=x.count('4')
    #Count of negative comments
    neg=len(x)-pos
    #Calculation of percentage
    pos_per=(pos/len(x))*100
    neg_per=(neg/len(x))*100
    return pos_per
    #print("Final Results Obtained:")
    #print("Postive Sentiment Percentage: ",pos_per,"\nNegative Sentiment Percentage: ",neg_per)