import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to PyPassword Generator")
letter=int(input("How many letters would you like in your password? \n"))
symbol=int(input("How many symbols would you like in your password? \n"))
number=int(input("How many numbers would you like in your password? \n"))

pw_list=[]
for char in range(0, letter):
    pw_list.append(random.choice(letters))

for char in range(0, symbol):
    pw_list.append(random.choice(symbols))
    
for char in range(0, number):
    pw_list.append(random.choice(numbers))
    # OR
    # pw_list+=random.choice(numbers)

random.shuffle(pw_list)
password=""
for pw_char in pw_list:
    password+=pw_char

print(f"Your password is {password}")
