# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:35:02 2020

@author: 17426
"""
#import matplotlib
import matplotlib.pyplot as plt

#put the DNA string in a string variable
s="ATGCTTCAGAAAGGTCTTACG"
#use a variable to store the length of the string
n=len(s)
#set the number of each type of nucleotides to 0
numA=0
numT=0
numC=0
numG=0
#the length of the DNA string is n, count every nucleotide
for i in range(0,n):
    if s[i]=="A":
        numA+=1
    elif s[i]=="T":
        numT+=1
    elif s[i]=="C":
        numC+=1
    else:
        numG+=1
#The above counting ATCG from the raw DNA sequence is optional according to the guidance. 
#I still keep it since it contains my correction according the formative feedback

#feel free to change the values for the counts of ATCG here
#numA=
#numT=
#numC=
#numG=
#create the frequency dictionary, 
frequency={'A':numA,'T':numT,'C':numC,'G':numG}
#print the frequency dictionary
print(frequency)

#pie chart where the slides will be ordered and plotted counter-clockwise
labels='A','T','C','G'
sizes=[numA,numT,numC,numG]
explode=(0,0,0,0)
#specifies the fraction of the redius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90)
#equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
#name the title of the pie chart
plt.title('pie of the four DNA nucleotides')
#output the plot
plt.show()
plt.close()