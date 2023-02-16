## Using .csv files  
csv stands for Comma Separated Values  

### Importing CSV  
import csv  
with open("filename.csv") as data_file:  
    data=csv.reader(data_file)  
    for row in data:  
        print('row')  

#### this prints everything in a list format line by line  
&nbsp;  

# Pandas  
Documentation: pandas.pydata.org  
It is not preinstalled like turtle. You have to install it separately on your own.  
#### Syntax:  
import pandas  
data=pandas.read_csv('filename.csv')  

This program helps to read .csv files using python easily in a tabular format even within the terminal  

## Data Structure in Python  
two primary types:  
1. Series (1-dimensional)  
2. DataFrame (2-dimensional)  
it can be checked by using type('data')  

Basically, the whole table is a DataFrame and every column is a Series (like a list)  

