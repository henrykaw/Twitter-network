#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:07:54 2017

@author: henrikkawa
"""
import pickle
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
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
    #load pickle file
    with open(comPath+file1,'rb') as f1:
        com1 = pickle.load(f1)
    #Count amount of members in the communities
    count_list = Counter(value for key, value in com1.items())
    #Get top 100 communities
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
        if file1 != file2:
            ##### LOAD SECOND FILE
            with open(comPath+file2,'rb') as f2:
                com2 = pickle.load(f2)
                
            #Count amount of members in the communities
            count_list = Counter(value for key, value in com2.items())
            #Get top 100 communities
            top_10_com = []
            for i in range(10):
                top_10_com.append(count_list.most_common(10)[i][0])
            dict_2 = {}
            
            for com in top_10_com:
                dict_2[com] = []
            
            
            for key, value in com2.items():
                if value in top_10_com:
                    dict_2[value].append(key)
    
            #Making confusion matrix
            cm_array = np.empty([10,10])
            namesRow = sorted([key for key, value in dict_1.items()])
            namesCol = sorted([key for key, value in dict_2.items()])
            
            for ix1, row in enumerate(namesRow):
                print(ix1)
                for ix2, col in enumerate(namesCol):
                    diff =1-len(set(dict_1[row]).symmetric_difference(set(dict_2[col])))/len(set(dict_1[row]).union(set(dict_2[col])))
                    cm_array[ix1][ix2] = diff
                    
            #Save Plot      
            df_cm = pd.DataFrame(cm_array, index = [i for i in namesRow],columns = [i for i in namesCol])
            plt.figure(figsize = (10,7))
            sn.heatmap(df_cm, annot=True)
            plt.savefig('confMat/comConMat_'+str(idx1)+'_'+str(idx2)+'.png')
            plt.show()