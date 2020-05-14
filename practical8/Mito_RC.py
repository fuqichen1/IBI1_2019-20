# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:20:39 2020

@author: 17426
"""

import re

file_name=input('Please input the filename: ')
a=False
length=0
gene=''
#open the fasta file
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',"r")
#open a new file according to the input name
out_fasta=open(file_name+".fa","w")
#write the first line
out_fasta.write('$ head -10 rc.fa\n')
for line in file:
    #search whether it is a mito gene
    if line.find(':Mito:')>-1:
        x=re.findall('>.*? gene:(\w*) gene_.*',line)
        #write the gene name into ().fa if it is a mito gene
        out_fasta.write('>'+x[0])
        a=True
        continue
    #write the mito gene's length and sequence into ().fa
    if a==True and not(line.startswith('>')):
       line=line[:-1]
       length=length+len(line)
       #get reverse complementary sequence
       line1=line.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
       line1=line1.upper()
       gene=gene+line1
       gene=gene[::-1]
    elif a==True and line.startswith('>'):
       out_fasta.write('  '+str(length)+'\n')       
       out_fasta.write(gene+'\n')
       length=0
       gene=''
       a=False
#close files
out_fasta.close()
file.close()
