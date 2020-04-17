# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:18:21 2020

@author: 17426
"""

# What does this piece of code do?
# Answer: find a prime number in the range of 2-100 or get the result of 1 (the number is randomly generated)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            p=False

     
print(n)