# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:37:02 2020

@author: 17426
"""

import re
a=False #label whether it is a mito gene
length=0
gene=''
#open the fasta file
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',"r")
#open a new file called "mito_gene.fa"
out_fasta=open("mito_gene.fa","w")
for line in file:
    #search whether it is a mito gene
    if line.find(':Mito:')>-1:
        x=re.findall('>.*? gene:(\w*) gene_.*',line)
        #write the gene name into mito_gene.fa if it is a mito gene
        out_fasta.write('>'+x[0])
        a=True
        continue
    #write the mito gene's length and sequence into mito_gene.fa
    if a==True and not(line.startswith('>')):
       line=line[:-1] 
       length=length+len(line)
       gene=gene+line
    elif a==True and line.startswith('>'):
       out_fasta.write('  '+str(length)+'\n')       
       out_fasta.write(gene+'\n')
       length=0
       gene=''
       a=False
#close the files
out_fasta.close()
file.close()
