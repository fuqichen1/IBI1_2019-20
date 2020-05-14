# -*- coding: utf-8 -*-
"""
Created on Fri May  8 20:10:36 2020

@author: 17426
"""

import numpy as np
import matplotlib.pyplot as plt
N=10000  #population size
S=9999   #susceptical
I=1      #infected
R=0      #recovered
beta=0.3
gamma=0.05
s=[S]
i=[I]
r=[R]
time=1000
#loop 1000 times
for a in range(0,time):
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
#plot the graph
plt.figure(figsize=(6,4),dpi =150)
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
plt.plot(list(range(time+1)), s,label='Susceptible')
plt.plot(list(range(time+1)), i,label='Infected')
plt.plot(list(range(time+1)), r,label='Recovered')
legend = plt.legend(loc='upper right', shadow=False)
#save figure
plt.savefig('SIR',type='png')
plt.show()
plt.close()