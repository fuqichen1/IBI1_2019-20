# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:27:57 2020

@author: 17426
"""
import pandas as pd

#read files
human=open('SOD2_human.fa','r')
mouse=open('SOD2_mouse.fa','r')
random=open('RandomSeq.fa','r')

#get three names/sequences
for line in human:
    if line.find('>')>-1:
        name_human=line[:-1]
    else:
        seq_human=line[:-1]
for line in mouse:
    if line.find('>')>-1:
        name_mouse=line[:-1]
    else:
        seq_mouse=line[:-1]
for line in random:
    if line.find('>')>-1:
        name_random=line[:-1]
    else:
        seq_random=line[:-1]

#close the files
human.close()
mouse.close()
random.close()

#I typed Blosum 62 table in a csv file
table=pd.read_csv('BLOSUM62.csv')
column=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']

#comparasion between human and mouse
score=0
edit_distance = 0 
for	i in range(len(seq_human)): 
    #calculate score according to BLOSUM62
    score+=table.iloc[column.index(seq_human[i]),column.index(seq_mouse[i])+1]    
    #count how many animo acids are not identical
    if seq_human[i] != seq_mouse[i]:
        edit_distance += 1 
print(name_human)
print(seq_human)
print(name_mouse)
print(seq_mouse)
#output the percentage identity (keep two decimals)
print('%.2f%%' % (100-edit_distance/len(seq_human)*100))
print(str(int(score))+'\n')

#comparasion between human and random
score=0
edit_distance =	0 
for	i in range(len(seq_human)): 
    #calculate score according to BLOSUM62
    score+=table.iloc[column.index(seq_human[i]),column.index(seq_random[i])+1]
    #count how many animo acids are not identical
    if seq_human[i] != seq_random[i]:		
        edit_distance += 1 
print(name_human)
print(seq_human)
print(name_random)
print(seq_random)
#output the percentage identity (keep two decimals)
print('%.2f%%' % (100-edit_distance/len(seq_human)*100))
print(str(int(score))+'\n')

#comparasion between mouse and random
score=0
edit_distance =	0 
for	i in range(len(seq_mouse)): 
    #calculate score according to BLOSUM62
    score+=table.iloc[column.index(seq_mouse[i]),column.index(seq_random[i])+1]
    #count how many animo acids are not identical
    if seq_mouse[i] != seq_random[i]:		
        edit_distance += 1 
print(name_mouse)
print(seq_mouse)
print(name_random)
print(seq_random)
#output the percentage identity (keep two decimals)
print('%.2f%%' % (100-edit_distance/len(seq_mouse)*100))
print(str(int(score))+'\n')