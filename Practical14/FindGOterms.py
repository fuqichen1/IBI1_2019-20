# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:22:06 2020

@author: 17426
"""
#The code takes about 30-40 seconds to run, please be patient! Thank you very much!

#import python libraries
import pandas as pd
import xml.dom.minidom


result=[]  #store the whole dataframe of 'autophagosome' related genes
sub_result=[]  #temporarily store every 'autophagosome' related gene
id_result=[]   #store every 'autophagosome' related gene's id(use this to find chlidnodes)
   #count the number of childnodes of every 'autophagosome' related gene
n=0            #count the number of every 'autophagosome' related gene
is_a=[] 
dic={}  #to record is_a for every term


#Parse the XML file into a DOM document object
DOMTree = xml.dom.minidom.parse("go_obo.xml")
#get the root element of the document
collection=DOMTree.documentElement
#get the list of 'term' elements
terms=collection.getElementsByTagName('term')
#find 'autophagosome' related genes, record the information of 'id', 'name','definition' in result
for term in terms:
        a=term.getElementsByTagName('defstr')[0].childNodes[0].data
        #get a dictionary of is_a and use it to find childnodes
        IDs=term.getElementsByTagName('id')[0]
        is_as=term.getElementsByTagName('is_a')
        for x in is_as:
            is_a.append(x.childNodes[0].data)
        dic[IDs.childNodes[0].data]=is_a[:]
        is_a.clear()
        #get the information of the first three columns
        if a.find('autophagosome')>-1:
            #record 'id'
            sub_result.append(term.getElementsByTagName('id')[0].childNodes[0].data)
            #store their ids in id_result (use this to find chlidnodes)
            id_result.append(term.getElementsByTagName('id')[0].childNodes[0].data)
            #record 'name'
            sub_result.append(term.getElementsByTagName('name')[0].childNodes[0].data)
            #record 'definition'
            sub_result.append(term.getElementsByTagName('defstr')[0].childNodes[0].data)
            #add every autophagosome gene into result
            result.append(sub_result)
            sub_result=[]

#count the childnode 
childnodes = []
continu=True
for i in id_result:
    m = []
    count = 0
    #find childnodes
    for j in dic:
        if i in dic[j]:
            count += 1
            m.append (j)
    n = m[:]
    if count>0:
        continu = False
    #find childnode's childnode until no childnood is found
    while continu == False :
        m = []
        continu = True
        for k in n:
            for j in dic:
                if k in dic[j]:
                    count += 1
                    continu = False
                    m.append (j)
        n = m[:]
    #record childnodes
    childnodes.append(count)

#add the number of the childnodes to the dataframe
for n in range(len(id_result)):
    result[n].append(str(childnodes[n]))
 
#output the result       
index=[]
n=len(id_result)
for i in range(n):
    index.append(i)
df1 = pd.DataFrame(result,
                    index,
                   columns=['id', 'name','definition','childnodes'])
df1.to_excel("autophagosome.xlsx",index=False)  