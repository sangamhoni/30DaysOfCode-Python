## Lists  
#### Syntax:
fav_number=[prime_number, "PI", 3.1415]  

#### Accesing the list items  
print(fav_number[1])        #gives PI  
print(fav_number[-1])       #gives 3.1415  
print(fav_number) 

#### Altering the data  
fav_number[0]="12357.."     #changes prime_number to 12357..  
fav_number.append("Eulers number")  #adds Eulers number to the list, can only add one data  
fav_number.extend(["Eulers number", 0, 69])     #adds multiple data at the end  

#### Lists inside a list  
fruits=["Apple", "Mango", "Strawberry", "Banana"]  
vegetables=["Spinach", "Tomatoes", "Celery", "Potatoes"]  
fruits_veggies=[fruits, vegetables]  

### Notes:  
- a single list can contain different data types  
- to add something in a list, either use list_name+= data OR list_name.append(data)  




### More on list here:  
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists  

## Other functions  
names="Sangam, Jay, Mandip, Dikshya"  
name1=names.split(", ")         #Output=["Sangam", "Jay", "Mandip", "Dikshya"]  