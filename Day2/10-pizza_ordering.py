print("Welcome to Python Pizza")
size = input("Which size pizza do you want? (S/M/L) ")

bill=0
if (size == "s" or size == "S"):
    bill = 15
elif (size == "m" or size == "M"):
    bill = 20
else:
    bill = 25

pepperoni = input("Do you want extra pepporoni? (Y/N) ")
if (pepperoni == "Y" or pepperoni == "y"):
    if (size == "s" or size == "S"):
        bill += 2
    else:
        bill += 3

cheese = input("Do you want extra cheese? (Y/N) ")
if (cheese == "y" or cheese == "Y"):
    bill += 1

print(f"Your total bill is ${bill}")
