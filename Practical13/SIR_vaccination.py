# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:40:16 2020

@author: 17426
"""

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4),dpi =150)
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
N=10000  #population size
for a in range(0,11):  
   V=int(N*a/10)   #vaccinated people
   S=9999-V
   I=1
   R=0
   #avoid S to be negative when a reaches 10
   if S<0:
       S=0
       I=0
       R=10000
   beta=0.3
   gamma=0.05
   s=[S]
   i=[I]
   r=[R]
   time=1000
   
   for b in range(0,time):
       #calculate current beta
       curr_beta=beta*I/N
       #rondom infection
       s_every=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
       S=S-s_every
       I=I+s_every
       #random recovery
       i_every=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
       I=I-i_every
       R=R+i_every
       s.append(S)
       i.append(I)
       r.append(R)
   #add curve to the plot
   plt.plot(list(range(time+1)), i,label=str(a*10)+'%')
legend = plt.legend(loc='upper right', shadow=False)
plt.savefig('SIR_vaccination',type='png')
plt.show()
plt.close()