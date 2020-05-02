# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:37:02 2020

@author: 17426
"""

import re

#open the fasta file
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',"r")
Mito_seq=re.findall(r'>.*:Mito:.*[ATCG\n]*',file.read())

file.close()

print(Mito_seq)

#import re
#
#myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
#
#M_seq=re.findall(r'(>.*?:Mito:.*[AGCT\n]+?)>',myfasta.read())
#
#myfasta.close()
#
#
#
#out_seq=[]
#
#outfasta=open("mito_gene.fa","w")
#
#for seq in M_seq:
#
#    seq=seq.replace('\n','')
#
#    outfasta.write(re.sub(r'>[^AGCT].*]',"> "+re.findall(r'gene:Q[\d]*',seq)[0]+" gene_length:"+str(seq.count("A")+seq.count("G")+seq.count("C")+seq.count("T"))+"\n",seq)+"\n")
#
#outfasta.close()

    
    
    
    
        
        
