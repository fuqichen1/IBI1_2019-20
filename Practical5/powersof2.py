# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:05:20 2020

@author: 17426
"""
#start with some number x, I assume that x is no larger than 8192=2**13
x=2019
#use a string to record the result
s=str(x)+" is "
#find the large power of n to small power of n
n=13
#when every power of n is found, x will be equal to x-2""n until x=0
#judge whether x is equal to 0
while x!=0:
       #if current n power of 2 is larger than x, we should reduce n
       if x<2**n:
          n=n-1
       #if current n power of 2 is smaller than x, that means we find the n
       else:
          #this if statement is to record the result and 
          #make sure there is no spare "+" appearing at the end of the string
          if x%2==0 and n!=1:
              s=s+"2**"+str(n)+" + "
          elif x%2==1 and n!=0:
              s=s+"2**"+str(n)+" + "
          else:
              s=s+"2**"+str(n)
          #minus 2**n to find the next n
          x=x-2**n
#output the result
print(s)
        
        
    
 