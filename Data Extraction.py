# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:03:05 2019

@author: Mohit
"""

import pandas as pd
import numpy as np
import os
import pyodbc

os.chdir("C:/Users/Mohit/Desktop/Nikhil Analytics Material/Python/Python Part 2/Class 7/Assignments")
os.getcwd()
os.listdir()
#Reading Text Files - read_table
data1=pd.read_table("company.txt",sep="/",header=None)
data1
data1.shape
#Reading CSV Files - read_csv
data2=pd.read_csv("crabtag.csv")
data2
data2.head()
data2.shape
#Reading Excel Files - read_excel
data3 = pd.read_excel("sales.xlsx")
data3
#Reading SAS files - read_sas
data4 = pd.read_sas("movies.sas7bdat")
data4.shape
data4['Movie'].head()


data5 = pd.read_sas("cars.sas7bdat")
data5

data6 = pd.read_csv("SampleCSVFile2.csv",encoding = "ISO-8859-8")
data6


data7 = pd.read_csv("SampleCSVFile3.csv")


data8 = pd.read_table("sampletxt3.txt")


# To read data from database, we need DSN(data source name)
# Steps to create DSN
# control panel->administrative  tool->odbc service
# user dsn->add->give name -> server name (check in database properties of sql server)
# no changes in next window->

import pyodbc
myconn = pyodbc.connect(DSN = "python_classs")
data_customer = pd.read_sql("select * from Product_Pivot",myconn)
print(data_customer)


#Reading Database Files - read_sql_table, read_sql_query, read_sql
conn=pyodbc.connect('DSN=dsn')
data5=pd.read_sql('select * from table',conn)
print(data5)
