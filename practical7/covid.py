# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:48:29 2020

@author: 17426
"""
#import python libraries
#import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change to the correct path
#os.chdir("/users/17426/Desktop/课程/大一/IBI1/Week 7 Public health informatics")
#Note that the above directory is my own computer's, to avoid that markers cannot read files on their computers I store the full_data in the same directory as code's. 

#import the csv file
covid_data = pd.read_csv("full_data.csv")


my_columns=[]
print(covid_data.iloc[0:16:3,0:6])
for i in range(0,7996) :
    if covid_data.iloc[i,1]=="Afghanistan":
       my_columns.append(True)
    else:
       my_columns.append(False)
print(covid_data.iloc[my_columns,4])

#world_new_cases.csv is a file which contains dates, world new cases and world new death
#I also uploaded world_new_cases.csv in practical 7 folder. 
covid_data_world = pd.read_csv("world_new_cases.csv")
#store world_new_cases, world_new_deaths, world_dates in arrays
world_new_cases=np.array(covid_data_world.iloc[:,1])
world_dates=np.array(covid_data_world.iloc[:,0])
world_new_deaths=np.array(covid_data_world.iloc[:,2])
#output mean and median of new cases for the entire world
print('mean: '+str(np.mean(world_new_cases)))
print('median: '+str(np.median(world_new_cases)))

#a boxplot of the new cases worldwide
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.title('a boxplot of new cases worldwide')
plt.ylabel("Number")
plt.show()
plt.close()

#plot both the new cases and new deaths worldwide
plt.title('a plot of new cases and new deaths worldwide')
plt.xlabel("Date")
plt.ylabel("Number")
plt.plot(world_dates,world_new_cases, 'b+',world_new_deaths,'m+')
plt.xticks(covid_data_world.iloc[:,0].iloc[0:len(world_dates):4],rotation=-90)
plt.show()
plt.close()

#the code to answver my question(How have new cases and total cases developed over time in spain?)
my_columns_spain=[]
for i in range(0,7996) :
    if covid_data.iloc[i,1]=="Spain":
       my_columns_spain.append(True)
    else:
       my_columns_spain.append(False)
spain_new_cases=np.array(covid_data.iloc[my_columns_spain,2])
spain_dates=np.array(covid_data.iloc[my_columns_spain,0])
spain_total_cases=np.array(covid_data.iloc[my_columns_spain,4])
plt.title('a plot of new cases and total cases in spain')
plt.xlabel("Date")
plt.ylabel("Number")
plt.plot(spain_dates,spain_new_cases, 'b+',spain_total_cases,'m+')
plt.xticks(covid_data.iloc[my_columns_spain,0].iloc[0:len(world_dates):4],rotation=-90)
plt.show()
plt.close()