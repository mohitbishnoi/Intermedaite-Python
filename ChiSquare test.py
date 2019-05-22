# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:12:49 2019

@author: Mohit
"""

Chi Square test -  is used to find association between two categorical values.

X**2  = E(observerd-expected)**2/expected

Categoriacal table:
    Gender       Result
    M               P
    F               P
    M               F
    F               F
    M               P
    F               F
    
    
H0 - there is no associstion between given variable
H1 - there is association between given variable

P value>=0.05 accept H0
P value<=0.05 reject H0
# if we are rejecting H0, then we have to accept H1

 Value of X**2  = 12.78, P value = 0.08
 Value of x**2 is dependent on P value
 
we will be getting x**2 value using chi square table
DF = Degree of freedom

import pandas as pd
import os
import numpy as np
from scipy.stats import chi2_contingency
os.chdir("C:/Users/Mohit/Desktop/Nikhil Analytics Material/Python/Python Part 2/Class 10")
Hair_eye = pd.read_table("Hair_Eye_Color.txt",header=0,delim_whitespace = True)
Hair_eye.shape

cont_table = pd.pivot_table(Hair_eye,values = ['n'],
                            index = ['Hair'],columns = ['Eye'],
                            aggfunc = np.sum)

#  As we have missing value, so we can chi square test for missing values.(NaN) is missing  value.
# Replace missing value with missing value

cont_table2=cont_table.replace(np.nan,0)

chitest_value,p_value,df,expected_vale = chi2_contingency(cont_table2)

print(p_value)

# as p_value = 0.073 <0.05, we reject H0.
# so accept association  between hair and eye color.

print(chitest_value) #20.92
# ChiSquare table value  = 15.507

Different Test at chisquare:
1. Test of association or test of independence (above test)
2. Goodness of fit (below)

Bank - 3 type of customer
                    Expected data       observerd data(with sample data)
        1- retail -    30%                  25%
        2 - salary -   30%                  40%
        3 - business - 40%                  35%
        
here:
    H0 - given sample is consistant with respected value
    H1 - given sample is not consistent with respected value
    P_Value >= 0.05 is good for use.
    
#Goodness of fit test
Expected_Data = [0.30,.30,.40]
Sample_Data = [75,105,120]

sample_percentage = Sample_Data/np.sum(Sample_Data)

from scipy.stats import chisquare

chitest_value,p_value=chisquare(f_obs=sample_percentage,f_exp=Expected_Data)

print(p_value)
# as p-value=0.992>0.05, we accept H0.
# so we accept sample data,as sample is consistent with expected_data

# degree of freedom = n-1 (3-1=2)

#x2test_value = 0.0166 < x2table_Value=5.991, so we accept H0













