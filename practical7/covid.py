# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:48:29 2020

@author: 17426
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/users/17426/Desktop/课程/大一/IBI1/Week 7")

covid_data = pd.read_csv("full_data.csv")
my_columns=[]
print(covid_data.iloc[0:16:3,0:6])
for i in range(0,7996) :
    if covid_data.iloc[i,1]=="Afghanistan":
       my_columns.append(True)
    else:
       my_columns.append(False)
print(covid_data.iloc[my_columns,4])

covid_data_world = pd.read_csv("world_new_cases.csv")
#I also uploaded world_new_cases.csv in my practical 7 folder. 
world_new_cases=np.array(covid_data_world.iloc[:,1])
world_dates=np.array(covid_data_world.iloc[:,0])
world_new_deaths=np.array(covid_data_world.iloc[:,2])
print(np.mean(world_new_cases))
print(np.median(world_new_cases))

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
plt.legend
plt.show()

plt.title('a plot of new cases and new deaths worldwide')
plt.plot(world_dates,world_new_cases, 'b+',world_new_deaths,'m+')
#plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()

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
plt.plot(spain_dates,spain_new_cases, 'b+',spain_total_cases,'m+')
plt.show()