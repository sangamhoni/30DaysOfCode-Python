print("Welcome to Love Calculator")

name1=input("Enter your name:  ")
name2=input("Enter their name: ")

name=name1+name2
name=name.lower()

t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")

true=int(t+r+u+e)
love=int(l+o+v+e)

love_score=true*10+love

print(f"Your love score is {love_score}")


