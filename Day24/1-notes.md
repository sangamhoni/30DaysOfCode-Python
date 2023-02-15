# File Handling  

### Opening a file  
#### For Reading  
file_var = open("filename.ext")  
OR  
with open("filename.ext") as file_var:  
with open("filename.ext", mode='r') as file_var:  
##### Doing this allows you to not close a file after using  
its in reading mode by default  
#### For Writing  
with open("filename.ext", mode='w') as file_var:

### Reading a file
contents=file.read()  
this stores all the contents of the file in the contents variable  

### Writing to a file  
with open("filename.ext", mode='w') as file_var:  
    file_var.write("New text")  

### Adding to a file  
with open("filename.ext", mode='a') as file_var  (mode='append'):
    file.write("\n New text")  

### Closing a file  
file.close()  
// Not needed for with open{"..."} method  

