# OOP  
&nbsp;  

## Methods  
- functions that are inside class  

&nbsp;  
## Class  
#### Creating a Class:  
class ClassName:  

### Initializing an object  
decides what should happen when the object is being constructed  
setting variables, counters, etc to their starting values  
#### Syntax:  
class ClassName:
    def __init__(self, var, user):
    # code here  
    self.varname=var  
    self.username=user  

It is called everytime an object related to the class is used  

&nbsp;  
# Notes:
- use 'pass' to run an empty function without indent error  
- camelCase is v similar to PascalCase, except the fact that camelCase's first letter is small  
- snake_case is where you separate the words with a '_'  

# Steps on using a package:  
1. import the class from the package  
    Eg: from turtle import Turtle  
2. create an object from the class  
    Eg: my_turt=Turtle()  
3. use the methods and attributes(fields) available as required  
    Eg: my_turt.forward()  