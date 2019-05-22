# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:59:44 2019

@author: Mohit
"""

# lambda function - is used to create temporary funtion to perfrom calculation

# syntex - lambda args:calcultion

f = lambda x,y:x+y 

print(f(10,20))
print(f(30,-10))

mylist = [1,2,3,4,5,6,7,8,9,10]
# incremaent all values of list with 5

mylist + 5 #  typeerror

# map function - is used to perfrom same calculation with all values of list
# syntax - map(lambda, list_name)

newlist = list(map(lambda x:x+5,mylist))

# filter function - is used to filter list data based on given condition.
# syntax - filter(lambda, list_name)

odd_list = list(filter(lambda x:x%2,mylist))

# how to get even list - write code for this

# reduce function  - is used to reduce list value to single value
# after calculation

from functools import reduce
cum_total = reduce(lambda x,y:x+y,mylist)
print(cum_total)

#in case you do not want to use these functions, then you can try list comprehension

mylist2 = [x+5 for x in mylist]
print(mylist2)

# =============================================================================
# 10 mod 3 -> 1 true
# 10 mod 2 - > 0 false
# =============================================================================

# class assignment
# 1. find all odd value between 20 to 50, store these values in a list












