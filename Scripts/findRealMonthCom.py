#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:54:36 2017

@author: henrikkawa
"""

import pickle
from os import listdir

comPath = '../communities/'
rePath = '../replyDict/'

comFiles = []
reFiles = []
#Get list of relevant community files
for file in listdir(comPath):
    if file.startswith('Communities_'):
        comFiles.append(file)
comFiles = sorted(comFiles)
print(comFiles)

for file in listdir(rePath):
    if file.startswith('replyDict_'):
        reFiles.append(file)
reFiles = sorted(reFiles)
print(reFiles)
hits = []
for reFile in reFiles:
    print('Opening ',rePath,reFile)
    openReFile = open(rePath+reFile,'rb')
    replyDict = pickle.load(openReFile)
    openReFile.close()
    print(rePath,reFile, ' Loaded')
    for comFile in comFiles:
        print('Opening ',comPath,comFile)
        openComFile = open(comPath+comFile,'rb')
        comDict = pickle.load(openComFile)
        openComFile.close()
        print(comPath,comFile,' Loaded')
        if set(comDict.keys()).issubset(set(replyDict.keys())):
            hits.append(('com: '+str(comFile),'reply: '+str(reFile)))
            print(comFile,' is a subset of ',reFile)
            
with open('../realMonthComList.pickle','wb') as save_file:
    pickle.dump(hits, save_file)
    print('hits successfully saved.')