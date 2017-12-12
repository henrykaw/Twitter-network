#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:43:27 2017

@author: henrikkawa
"""

from os import listdir
import msgpack
import pandas as pd


files = []
csvPath ='../usedCsv/'
msgPath = '../newReplyDict/'
#Get list of relevant files
for file in listdir(csvPath):
    if file.startswith('csv_'):
        files.append(file)
files = sorted(files)
print(files)

for f in files:
    replyDict={}
    df = pd.read_csv(f, names=['id1','id2'], usecols=['id1','id2'])
    print("df loaded")
    count = 0
    for row in zip(df['id1'], df['id2']):
        count += 1
        if row[0] in replyDict:
            if row[1] not in replyDict[row[0]]:
                replyDict[row[0]].append(row[1])
        else:
            replyDict[row[0]] = [row[1]]
        if row[1] in replyDict:
            if row[0] not in replyDict[row[1]]:
                replyDict[row[1]].append(row[0])
        else:
            replyDict[row[1]] = [row[0]]
        if(count % 10000000 ==0):
            print(count)
    print("Dict loaded")
    with open(msgPath+'msgReplyDict_'+f[4:6], 'w') as out_file:
        msgpack.pack(replyDict, out_file)
    print('replyDict succesfully saved as msgpack')