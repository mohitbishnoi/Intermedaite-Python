# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:16:39 2019

@author: Mohit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import seaborn as sns

np.random.seed(10)
x = np.random.randn(1000)
len(x)
#to check for normal distribution
sns.distplot(x,hist= True,kde = True) #plotting histogram, kde is for line
pd.DataFrame(x).skew() # negitive value is below the line
pd.DataFrame(x).kurt() # postive value is histogeam peak is above the line

y = x+np.random.normal(0,10,1000)
plt.scatter(x,y)

np.corrcoef(x,y)

# r = 0.08558352 positive strong correlation

# correlation test - to check correlation test we are calculating is accepted for population or not

# correlation hyptothesis test -  we have to take sum some assumptions

# H0(null hypothesis) - correlation is equal to zero
# H1(alternative hypothesis) - correlation is equal not to zero

# p value - if p>=0.05 (significance level), then accept H0
#            if p> 0.05, then reject H0, and accept H1
# P is probablity (probablity of rejection or acceptence)


# correlation is accepted when p value is less than 0.05

pearsonr(x,y)

# (r = 0.08558352026965955, p-value = 0.006769546351106802)

# conclusion -  As p-value is less then 0.05, so we reject H0 and accept H1,
#               that means correlation between x and y is not equal to zero


data=pd.DataFrame({'x':x,'y':y})
data.shape
data['x'].corr(data['y'])
data.corr()  # return correlation matrix

# Numpy and pandas does not give p value

