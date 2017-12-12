
# coding: utf-8

# In[1]:


import pandas as pd
from os import listdir
from collections import Counter
import json

files = []
replyDict = {}

#Get list of relevant files
for file in listdir():
    if file.startswith('csv_'):
        files.append(file)
files = sorted(files)
print(files)

for i,f in enumerate(files, start=1):
    degreeDict = {}
    replyDict = {}
    degreeList = []
    print(f)
    df = pd.read_csv(f, names=['id1','id2','weigth'],nrows=1000000, dtype={'id1':str,'id2':str}, usecols=['id1','id2'])
    print("df loaded")
    for index,row in df.iterrows():
        if row['id1'] in replyDict:
            if row['id2'] not in replyDict[row['id1']]:
                replyDict[row['id1']].append(row['id2'])
        else:
            replyDict[row['id1']] = [row['id2']]
        if row['id2'] in replyDict:
            if row['id1'] not in replyDict[row['id2']]:
                replyDict[row['id2']].append(row['id1'])
        else:
            replyDict[row['id2']] = [row['id1']]
        if(index % 1000000 ==0):
            print(index)
    print("Dict loaded")
    for item in replyDict:
        degreeList.append(len(replyDict[item]))
    degreeDict = dict(Counter(degreeList))
    with open('replyDict_csv_'+str(i)+'.json', 'w') as fp1:
        json.dump(replyDict, fp1)
    with open('degree_result_csv_'+str(i)+'.json', 'w') as fp2:
        json.dump(degreeDict, fp2)
