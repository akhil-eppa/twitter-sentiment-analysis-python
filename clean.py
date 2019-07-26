# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:16:15 2019

@author: Akhil
"""
'''
import csv
f = open('training1.csv', 'rt')
reader = csv.reader(f,delimiter=',')
for row in reader:
    print(row[0] + "," + row[5])
'''
import preprocess
import csv
file1=open("training1.csv","rt")
file2=open("training3.csv","w")
writer = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\r')
reader=csv.reader(file1,delimiter=",")
for row in reader:
    temp=preprocess.process(row[5])
    writer.writerow([temp,row[0]])