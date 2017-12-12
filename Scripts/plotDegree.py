#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:20:48 2017

@author: henrikkawa
"""

import json
import operator
import matplotlib.pyplot as plt

months = ['January','February','March', 'April','May','June', 'July','August',
          'September','October','November','December']
for idx, file in enumerate(['degree_result_csv_01.json','degree_result_csv_02.json','degree_result_csv_03.json',
             'degree_result_csv_04.json','degree_result_csv_05.json','degree_result_csv_06.json',
             'degree_result_csv_07.json','degree_result_csv_08.json','degree_result_csv_09.json',
             'degree_result_csv_10.json','degree_result_csv_11.json','degree_result_csv_12.json']):
    plt.figure(figsize=(10,7),dpi=300)
    with open('degree_result/'+file, 'r') as f:
        data = json.load(f)
    sorted_x = sorted(data.items(), key=operator.itemgetter(1))
    plt.title('loglog degree distribution -'+months[idx])
    plt.ylabel('P_k')
    plt.xlabel('k')
    plt.loglog(list(data.keys()),list(data.values()),'bo')
    plt.savefig('degree_loglog/degree_distribution_loglog_'+file[18:20]+'.png')
#for item in sorted_x:
#    print(item)