# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:09:56 2020

@author: 17426
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population 
population=np.zeros((100,100))
#randomly choose one infected person
outbreak=np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]]=1     #1 represents infected, 0 represents susceptible, 2 represents recovered
#plot the result which includes the susceptible or infected people
plt.figure(figsize=(6,4),dpi=150) 
#Plot of rondom selection of one infected individual
plt.imshow(population,cmap='viridis',interpolation='nearest')
#set up model parameters (beta and gamma)
beta=0.3
gamma=0.05

#loop 100 times 
for a in range(1,101):
   # find infected points
   infectedIndex = np.where(population==1)
   # loop through all infected points
   for i in range(len(infectedIndex[0])):
       # get x, y coordinates for each point
       x = infectedIndex[0][i]
       y = infectedIndex[1][i]
       # infect each neighbour with probability beta
       # infect all 8 neighbours
       for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # don't infect yourself!
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
   #refind the infected people
   infectedIndex = np.where(population==1)
   # recover
   for b in range(len(infectedIndex[0])):
        x = infectedIndex[0][b]
        y = infectedIndex[1][b]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]  # gamma people recovered (assigned to 2)
   #plot the result when time=10, 50, 100
   if a==10 or a==50 or a==100:
     plt.figure(figsize=(6,4),dpi=150) 
     plt.imshow(population,cmap='viridis',interpolation='nearest')

#total 4 plots (start(time=0, also the plot of rondom selection of one infected individual), time=10, time=50, time=100)
                    