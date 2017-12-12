#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:54:56 2017

@author: henrikkawa
"""
import pickle
import pandas as pd
from collections import Counter
#Var
data = []
months = ['Jan_','Feb_','Mar_','Apr_','May_','Jun_']

#Paths
confPath = 'confMat/'
comPath='communities/'

#Files
confMatFiles = ['comMat_0_1.csv','comMat_1_2.csv','comMat_2_3.csv',
                'comMat_3_4.csv','comMat_4_5.csv']
comFiles = ['Communities_01.pickle','Communities_02.pickle',
            'Communities_03.pickle','Communities_04.pickle',
            'Communities_05.pickle','Communities_06.pickle']
for idx, (comFile1, comFile2) in enumerate(zip(comFiles[:5],comFiles[1:])):
    with open(comPath+comFile1, 'rb') as f1, open(comPath+comFile2, 'rb') as f2:
        
        #Loading communities and stuff
        print('Opening '+comFile1+'...')
        com1 = pickle.load(f1)
        count_list = Counter(value for key, value in com1.items())
        com1_top_10 = count_list.most_common(10)
        print('Opening '+comFile2+'...')
        com2 = pickle.load(f2)
        count_list = Counter(value for key, value in com2.items())
        com2_top_10 = count_list.most_common(10)
        
        #Creating dict with top 10 com with value consisting of node ids
        dict_1 = {}
        for i in range(10):
            dict_1[com1_top_10[i][0]] = []
        for key, value in com1.items():
            if value in dict_1.keys():
                dict_1[value].append(key)
        dict_2 = {}
        com2_10_list = []
        for i in range(10):
            dict_2[com2_top_10[i][0]] = []
            com2_10_list.append(com2_top_10[i][0])
        for key, value in com2.items():
            if value in dict_2.keys():
                dict_2[value].append(key)
                
        #loading confMat_array
        df = pd.read_csv(confPath+confMatFiles[idx], index_col=0)
        df[df<0.009] = 0
        for i, com1Num in enumerate(com1_top_10):
            for ix, similarity in enumerate(df.loc[com1Num[0]]):
                if similarity is not 0:
                    dfCom2Idx = int(df.columns[ix])
                    transValue = len(set(dict_1[com1Num[0]]))*(len(set(dict_1[com1Num[0]]).intersection(set(dict_2[dfCom2Idx])))/len(set(dict_1[com1Num[0]])))
                    transValue = round(transValue,0)
                    if transValue > 1000:
                        data.append([months[idx]+str(i+1),
                                     months[idx+1]+str(com2_10_list.index(dfCom2Idx)+1),
                                     transValue])
#                    if sankey_df is not None:
#                        temp_df = pd.DataFrame([[months[idx]+str(i+1),
#                                                months[idx+1]+str(com2_10_list.index(dfCom2Idx)+1),
#                                                transValue]],
#                                                columns=['Source','Target','Value'])
#                        print('appending to sankey_df')
#                        sankey_df.append(temp_df, ignore_index=True)
#                        print('appended to sankey_df')
#                    else:
#                        print('ini sankey_df')
#                        sankey_df = pd.DataFrame([[months[idx]+str(i+1),
#                                                months[idx+1]+str(com2_10_list.index(dfCom2Idx)+1),
#                                                transValue]],
#                                                columns=['Source','Target','Value'])
sankey_df = pd.DataFrame(data, columns=['Source','Target','Value'])
sankey_df.to_csv('sankeyValues.csv')
#df = pd.read_csv('confMat/comMat_0_1.csv', index_col=0)
#df[df<0.009] = 0