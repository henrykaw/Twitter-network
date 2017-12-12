#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:23:26 2017

@author: henrikkawa
"""

import pickle
from os import listdir
from collections import Counter

files = []
for file in listdir('communities'):
    if file.startswith('Com'):
        files.append(file)
files= sorted(files)

#def getStats(file):
with open('communities/Communities_01.pickle', 'rb') as fp:
    com = pickle.load(fp)
    count_list = Counter(value for key, value in com.items())
    top_10= count_list.most_common(10)
    print(len(com))
    for i in range(10):
        print(top_10[i][0],':',top_10[i][1])

#getStats('communities/Communities_01.pickle')