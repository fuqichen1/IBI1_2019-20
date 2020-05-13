# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:32:20 2020

@author: 17426
"""

#collatz sequence
#Create a new variable n. Assign it to a random positive integer.And print n
n=102
print(n)
#Repeat until n is equal to 1:
while n != 1: 
#     If n is even, n will be divided by 2.
      if n%2 == 0:   
         n=n/2
#     if n is odd, multiplying by 3 and adding 1
      else:     
         n=n*3+1
#     output the result
      print(n)    