# List Comprehension  
only available in python  
new_list=[new_item for item in list]  
#### decrease:  
numbers=[1, 2, 3]  
new_list=[]  
for n in numbers:  
    add_1 = n+1  
    new_list.append(add_1)  
#### to:  
new_list=[n+1 for n in numbers]  

it can also be used in strings  


# Conditional list comprehension  
new_list=[new_item for item in list if test]  
&nbsp;  

# Dictionary Comprehension  
new_dict={new_key:new_value for item in list}  
new_dict={new_key:new_value for (key, value) in dict_name.items()}  

## Looping through ditionary  
for (key, value) in dict_name.items():  
    print(key)  
    print(value)  

## converting dict to dataframe  
import pandas  
dataframe_format=pandas.DataFrame(dict_name)  

## Looping thru each rows in a dataframe  
for (index, row) in dataframe_format.iterrows():  
    print(row)  
    print(row.student)      // gives each of the student inside data frame  
  

// Here, row is the series in the dataframe  
