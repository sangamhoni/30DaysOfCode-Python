# Inheritance  
#### Syntax for inheritance:  
class ClassName(SuperClass):  
    def __init__(self):  
        super().__init__()  
#### Here, ClassName is inheriting from the SuperClass  
SuperClass is called the super class  

#  

# Slicing  
#### can be used with lists, tuple, etc.  
keys=['a', 'b', 'c', 'd', 'e', 'f', 'g']  

print(keys[1:4])  
#### prints b c d  

print(keys[4:])  
#### prints e f g  

print(keys[:4])  
#### prints a b c d  

print(keys[1:5:2])  
#### prints b d f  

print(keys[::2])  
#### prints a c e  

print(keys[::-1])  
#### prints g f e d c b a  
