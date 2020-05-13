# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=123
b=123123
print(b%7)  #check whether b can be divided by 7
c=b/7
d=c/11
e=d/13
print(a>e) #compare a to e. If the output is true, a is bigger than e. 

X= True
Y= False
Z=(X and not Y)or(Y and not X) 
print(Z)     #verify that Z is true if either X or Y (but not both) are true
W=(X!=Y)
print(W==Z)  #check whether W and Z are always the same, no matter the values of X and Y