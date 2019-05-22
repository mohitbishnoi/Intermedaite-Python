# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:16:13 2019

@author: Mohit
"""

Significance test - is used to compare group mean value(to find relation between two values)
                    (also called as t- test)
Types of test

A. One Sample Test          H0:Population mean =  value
                            H1:Population mean != value
                            (it will have 2 rejection region,  also called as two tail test)
                            Syntex: ttest_1samp(x,value)

B. Two Sample Test 
    1. unpaired t-test        H0:Mean1 = Mean2
                              H1:Mean1 != Mean2
                              syntex : ttest_ind(x,y) # independent
                
    2. paired t-test          H0:Mean1-Mean2 = 0
                              H1:Mean1-Mean2 != 0
                              ttest_rel(x,y) # relative
                            
Conclusion : if p-value >= 0.03, Accept H0
             if p-value <  0.05, Reject H0:
             if you reject H0, then we have to accept H1:
                 
                 
Identify variable:
    1. character : create group
    2. Numeric : analysis var

    
if value is coming beyond accepting area then we will reject them. if they are in acceptable area, we will accept them.:
    
acceptance area: 30     40      45
              
              29            42
              
             Here we will reject 29, we will accept 42.
             
Confidence interval:
    Mean +- z*6%
    Mean - Sample Mean
    z - constant = 1.96 at 95%
    std error = std/sqrt(sample size)
    std(sigma),sample size(n)
    
    
Type 1 error : we reject null hypothesis when it should be accepted.
                (because of high value of rejection region)
                (Pharma industries)
                
Type 2 error : we accept null hypthesis when it should be rejected.
                (because of low value of rejection region)
                (E commerse)
                
if H0: Population Mean<=value
    H1: population Mean >value
    (it will have one, right rejection region, also called as right tail test )

if H0 :Population Mean >= value
    H1 : Popultion Mean < value
    (it will have one, left rejection region, also called as left tail test)
    
-----------------------
In every test we will get two values
1. T value (optional)
2. P value (Mandatory)

In case of T value:
    we will check t value from T table (n <=30)
                                Z table(n > 30)
                                n is sample size
                                
t test become z, when it exceded the value of limit.



















