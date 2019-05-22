# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:09:25 2019

@author: Mohit
"""

import os
import numpy as np
import pandas as pd

#1. Extract Given data into Python
os.chdir("C:/Users/Mohit/Desktop/Nikhil Analytics Material/Python/Python Part 2/Class 9")
os.getcwd()
data = pd.read_excel('Assignment.xlsx')

#2. Find number of missing values of each variable
data.isnull().sum()
data1=data
#3. Replace numeric missing values by median
data2=data1.fillna(data1.median())

# 4. Replace charcter missing values by next value
data3 = data2.replace(method='bfill')

# 5. Find average height and wight for each group of sex
data4 = data.groupby(by='Sex')['Height','Weight'].mean()

#6. Replace male missing values of height with average height of male and female missing value of height with average height of female.
data_female = data[data['Sex']=="F"]
data_male = data[data['Sex']=="M"]
data_female["Height"]=data_female["Height"].replace(np.nan,165.33)
data_male["Height"]=data_male["Height"].replace(np.nan,170.25)

data_female
data5= pd.concat([data_male,data_female])
data5