#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:08:18 2017

@author: henrikkawa
"""
import pickle
import pandas as pd
from collections import Counter
import numpy as np
from os import listdir

comPath = '/Users/henrikkawa/Desktop/twitter_dump/communities/'
comFiles = []
#Get list of relevant community files
for file in listdir(comPath):
    if file.startswith('Communities_'):
        comFiles.append(file)
comFiles = sorted(comFiles)
print(comFiles)

for idx1,file1 in enumerate(comFiles):
    with open(comPath+file1, 'rb') as f1:
        print('Opening file: ',file1)
        com1 = pickle.load(f1)
        count_list = []
        count_list = Counter(value for key, value in com1.items())
        top_10_com = []
        for i in range(10):
            top_10_com.append(count_list.most_common(10)[i][0])
        dict_1 = {}
        for com in top_10_com:
            dict_1[com] = []
        for key, value in com1.items():
            if value in top_10_com:
                dict_1[value].append(key)
        
        for idx2, file2 in enumerate(comFiles):
            if file2 != file1:
                print('At ',file1,'/',file2)
                with open(comPath+file2, 'rb') as f2:
                    com2 = pickle.load(f2)
                    print('Opened file ', file2)
                    count_list = []
                    count_list = Counter(value for key, value in com2.items())
                    top_10_com = []
                    for i in range(10):
                        top_10_com.append(count_list.most_common(10)[i][0])
                    dict_2 = {}
                    for com in top_10_com:
                        dict_2[com] = []
                    for key, value in com2.items():
                        if value in top_10_com:
                            dict_2[value].append(key)
                    cm_array = np.empty([10,10])
                    namesRow = sorted([key for key, value in dict_1.items()])
                    namesCol = sorted([key for key, value in dict_2.items()])
                    
                    print('calculating similarity')
                    for ix1, row in enumerate(namesRow):
                        for ix2, col in enumerate(namesCol):
                            diff =1-len(set(dict_1[row]).symmetric_difference(set(dict_2[col])))/len(set(dict_1[row]).union(set(dict_2[col])))
                            cm_array[ix1][ix2] = diff

                    df_cm = pd.DataFrame(cm_array, index = [i for i in namesRow],columns = [i for i in namesCol])
                    df_cm.to_csv('comMat_'+str(idx1)+'_'+str(idx2)+'.csv')
                    print('confMat/dataframe saved')