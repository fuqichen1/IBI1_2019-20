# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:43:07 2020

@author: 17426
"""
#input the list of 10 values
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#create a copy of the list
gene_lengths_copy=gene_lengths[:]
#sort the copied list
gene_lengths_copy.sort()
#get the value of the biggest and smallest gene lengths
max=gene_lengths_copy[9]
min=gene_lengths_copy[0]
#remove the longest and shortest gene lengths
gene_lengths.remove(max)
gene_lengths.remove(min)
#print the list with the longest and shortest gene lengths removed
print(gene_lengths)

#import matplotlib
import matplotlib.pyplot as plt
#set the boxplot
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
#boxplot output
plt.show()