# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:46:19 2019

@author: Akhil
"""
#loading the necessary packages
import tweepy
import pandas as pd
import csv
import preprocess
import time
import json

def start_collection(handle):
    file=open('tweet_testing2.csv','w')
    csvwriter=csv.writer(file,lineterminator='\r')
    with open('twitter_credentials.json') as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api=tweepy.API(auth)
    i=0
    t1=time.time()
    for tweet in tweepy.Cursor(api.search,q=handle,count=10000,lang="en").items():
                                   csvwriter.writerow([tweet.text.encode('utf-8')])
                                   i=i+1
                                   t2=time.time()
                                   if i==1000:
                                       break
                                   elif t2-t1>=45.0:
                                       break
                                   else:
                                       pass                               
    file.close()
    #Method 1==>    
    df=pd.read_csv('tweet_testing2.csv')
    df.drop_duplicates(subset=None,inplace=True)
    df.to_csv('trial3.csv')
    #df.close()
    file1=open("trial3.csv","rt")
    file2=open("trial4.csv","w+")
    print("Preprocessing of downloaded tweets has begun....")
    writer = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\r')
    reader=csv.reader(file1,delimiter=",")
    for row in reader:
        temp=preprocess.process(row[1])
        writer.writerow([temp])
    file1.close()
    file2.close()
