## Global variable  
To use a global variable inside a function and modify it for the function, use 'global var_name'  
Eg:  
enemies=1  
def increase_enemy():  
    global enemies  
    enemies+=1  
    print(enemies)      //gives 2  
print(enemies)          //gives 2

## Notes  
- To declare something a global variable (such as PI), we can write the var name in uppercase instead of writing global varname (PI=3.141, URL="https://www.google.com")  


