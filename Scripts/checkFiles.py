#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:18:58 2017

@author: henrikkawa
"""
same = 0
diff = 0
count = 0
with open('csv_01.csv') as f1, open('csv_02.csv') as f2:
    try:
        for x,y in zip(f1,f2):
            count += 1
            if x == y:
                same += 1
            else:
                diff += 1
            if (count % 1000000 == 0):
                print(count)
    except:
        pass
            
print('same: ',same,'diff: ', diff)