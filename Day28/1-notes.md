# Tkinter  
- Tkinter is a module used to implement GUI using python  
- It is auto installed module with python  
Syntax:  
import tkinter  
window=tkinter.Tk()  
window.mainloop()  

### Useful classes in tkinter  
- Entry()  
to create a box where the user can enter value  
- Label(text="...")  
to create a printed text  
- Button(text="...")  
to create a clickable button  


# *Args and **Kwargs  
&nbsp;  

## *Args  
*args collects the value in a tuple  (1, 2, 3, 4)  
def add(*args):  
    for n in args:  
        print(n)  

It can be called anything instead of *args in the function  

## **Kwargs  
kwargs stands for Keywords Arguments  
it collects the value in a dictonary {'add': 3, 'multiply': 9}  

def calculate(**kwargs):  
    print(kwargs)  
    for key, value in kwargs.items():  
        print(key)  
        print(value)  

calculate(add=3, multiply=9)  

## More on TK  
https://www.tcl.tk/man/tcl/TkCmd/contents.html  