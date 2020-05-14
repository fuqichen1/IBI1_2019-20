# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:10:18 2020

@author: 17426
"""
#input sequence
seq = 'ATGCGACTACGATCGAGGGCCAT'
#use a variable to store the length of the string
n=len(seq)
#use a string variable to store the output
output=''
i=0
#reverse every neucleotide
for i in range(0,n):
    if seq[i]=="A":
        output=output+'T' 
    elif seq[i]=="T":
        output=output+'A'
    elif seq[i]=="C":
        output=output+'G'
    else:
        output=output+'C'
    i+=1
#reverse the sequence
output=output[::-1]
#output the result
print(output)