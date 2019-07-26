# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:06:33 2019

@author: Akhil
"""
#Importing all the necessary packages
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
from sklearn import svm
import pandas as pd
import pickle
import numpy as np
#Loading the training set
file=open("training3.csv","rt")
#data is for storing all tweets from training set
data=[]
#labels is for storing (4/0) for all tweets from training set
labels=[]
reader=csv.reader(file,delimiter=",")
for row in reader:
    if row[0]!='':
        data.append(row[0])
        labels.append(row[1])
file.close()
half=796343
#data2 is used to store 20,000 tweets from data
data2=[]
#labels2 is used to store 20,000 (4/0) from labels
labels2=[]
#data2=data[0:1000]+data[half:half+10000]
data2=data[0:1000]+data[100000:101000]+data[200000:201000]+data[300000:301000]+data[400000:401000]+data[500000:501000]+data[600000:601000]+data[700000:701000]+data[350000:351000]+data[575000:576000]+data[half:half+1000]+data[half+100000:half+101000]+data[half+200000:half+201000]+data[half+300000:half+301000]+data[half+400000:half+401000]+data[half+500000:half+501000]+data[half+600000:half+601000]+data[half+700000:half+701000]+data[half+350000:half+351000]+data[half+575000:half+576000]
labels2=labels[0:10000]+labels[half:half+10000]

labels2=labels[0:1000]+labels[100000:101000]+labels[200000:201000]+labels[300000:301000]+labels[400000:401000]+labels[500000:501000]+labels[600000:601000]+labels[700000:701000]+labels[350000:351000]+labels[575000:576000]+labels[half:half+1000]+labels[half+100000:half+101000]+labels[half+200000:half+201000]+labels[half+300000:half+301000]+labels[half+400000:half+401000]+labels[half+500000:half+501000]+labels[half+600000:half+601000]+labels[half+700000:half+701000]+labels[half+350000:half+351000]+labels[half+575000:half+576000]
labels2=np.array(labels2)

#Tfidf vectorization of tweets in training set for training the model
vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             sublinear_tf = True,
                             use_idf = True)
train=vectorizer.fit_transform(data2)
#Creating a gausian kernel svm classifier 
classifier=svm.SVC(kernel="linear",random_state=0)
classifier.fit(train,labels2)
#Pickling the classifier and the Vectorizer so that it can be used in the future.
with open("model.pkl","wb") as file:
    pickle.dump((vectorizer,classifier),file)


#Below code can be executed in a separate module to make the computation time less by
#prevention of compilation of entire above code everytime the model is run

'''
df=open("test_set.csv","rt")
reader2=csv.reader(df,delimiter=",")
test=[]
for row in reader2:
    if row[0]!='':
      test.append(row[0])
print(len(test))
test_vectors = vectorizer.transform(test)
predicted=classifier.predict(test_vectors)
x=predicted.tolist()
print(x.count('4'))

with open('model.pkl', 'rb') as f:
    vct,clf = pickle.load(f)
test_vectors2=vct.transform(test)
pred2=clf.predict(test_vectors2)
x=pred2.tolist()
print(x.count('4'))
'''