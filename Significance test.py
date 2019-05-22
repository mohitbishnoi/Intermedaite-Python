# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:23:30 2019

@author: Mohit
"""

import pandas as pd
from scipy import stats

data = pd.read_csv('C:/Users/Mohit/Desktop/Nikhil Analytics Material/Python/Python Part 2/Class 10/brain_size.csv',sep = ';',na_values = '.')
data

data.head()

#one sample test
#H0 mean VIQ is equal to 100
#H1 maan VIQ is not equal to 100

stats.ttest_1samp(data['VIQ'],100)

# conclusion:
# as p value = 0.00203 is less then 0.05, so we rejct H0.
# means VIQ is not equal to 100


# two sample test
# H0: mean VIQ of female is equal to mean VIQ of male
# H1: mean VIQ of female is not equal to mean VIQ of male

male_VIQ = data[data['Gender']=='Male']['VIQ']
female_VIQ= data[data['Gender']=='Female']['VIQ']

stats.ttest_ind(female_VIQ,male_VIQ)

# Conclusion:
# As pvalue = 0.4445 is more then 0.05, so we accept H0.
# mean female_VIQ is equal to male_VIQ

#Write code to compare height of male with height of female
# H0 : average height of female is equal to average height of male
# H1 : average height of female is not equal to average height of male

male_height = data[data['Gender']=='Male']['Height']
female_height = data[data['Gender']=='Female']['Height']
import numpy as np
male_height2 =round(male_height.replace(np.nan,np.mean(male_height)),2)

stats.ttest_ind(female_height,male_height2)
# Conclusion:
# As pvalue = 1.38749301978548e-07 is less then 0.05, so we reject null.
# average height of female is not equale to average height of male.



#paired t test
# H0 : average VIQ before training is equal to average VIQ after training.
# H1 : average VIQ before training is not equal to average VIQ after training.

before_trainig= data['FSIQ']
after_training=data['PIQ']

# H0 : difference between before training and after training is equal to zero.
# H1 : difference between before training and after training is not equal to zero.

stats.ttest_rel(before_trainig,after_training)

#Conclusion:
# as pvalue=0.08217 is more then 0.05, so we accept H0.
# average VIQ before training is equal to average VIQ after training.



