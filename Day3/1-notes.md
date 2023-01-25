## Random Module  
#### Syntax:  
import random  
random.randint(i, j)  
random.randrange()  
random.random()     #gives random float num from 0-1 (not including 1)  

##### Eg:   
print("random range= ", random.randrange(100, 200))  
print("random range= ", random.randint(100, 200))  

#### Notes:  
- A range in python is something that includes the lower-bound but does not include the upper-bound. At first, this may seem confusing but it is intentional and it is used throughout python.  


## Making our own module:
1. make a new py file "mymodule.py" and enter pi=3.1415  
2. now import it in another program using _import mymodule_  
3. you can then use that value using syntax _mymodule.pi_  