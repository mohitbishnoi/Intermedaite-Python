# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:24:35 2019

@author: Mohit
"""

# =============================================================================
# # Any data given to  us, what we going to do
# =============================================================================

# =============================================================================
# # First step = we try to understand the data by calculating discriptive statistics
# 
# # stastics
# #1. Central Tendency - Mean/Median/Mode
# #2. Dispersion       - Variance/std/quantiles
# #3. Skewness         - Spreadness of data along with mean
# #4. Kurtosis         - frequency of data,probablity of data
# =============================================================================

import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))

data.describe()
data['A'].skew()
data['A'].kurt()

import seaborn as sns

# =============================================================================
# Discriptive Statistics -
# 
# 1. Central Tendency - is used to find mid point of data
# 1.1  Mean - Sum of all value/count of all value
# 1.2 Median - Middle most value after ascending order of sorting
# 1.3 Mode - Most frequently occuring values # we dont have any system defind function for mode
# # in case of character/string value we use mode. Mean and median will not work there
# 
# 2. Dispersion
# 2.1 Variance - Average deviation from mean  (E1 to n (xi-mean)**2/n-1)
# 2.2 Std - More deviation is not preferable(small deviation prefreable)  Squareroot of variance
# 2.3 Quantiles - 25% of data is Q1 (Quantile 1)
#                 50% of data is Q2 (Quantile 2)
#                 75% of data is Q3 (Quantile 3)
#                 # Rest data is extremly high or extremly low, that's why ignored by system.
#                 
# 3. Skewness  -Spreadness data along with mean (df['A'].skew)
# 4. Kurtosis - data is at peak. (working with least market(selected people) or widesest market(all together))
# (df.['A'].Kurt())
# 
# =============================================================================
