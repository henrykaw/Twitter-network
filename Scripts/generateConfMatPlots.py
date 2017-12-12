#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:48:53 2017

@author: henrikkawa
"""
import pandas as pd
from os import listdir
import seaborn as sns
import matplotlib.pyplot as plt
files = []
for file in listdir('confMat'):
    if file.startswith('comMat'):
        files.append(file)
files = sorted(files)
print(files)
for file in files: 
    plt.figure(dpi=300)
    df = pd.read_csv('confMat/'+file, index_col=0)
    df[df<0.009] = 0
    #df.clip(lower=0.0001,upper=1, inplace=True)
    plt.title('Confusion Matrix')
    ax = sns.heatmap(df,vmin=0,vmax=1,annot=True,fmt='.2g')
    ax.set(ylabel=file[7:8], xlabel=file[9:10])
    plt.savefig('confMat/confMatPlot_'+file[7:8]+'_'+file[9:10]+'.png')