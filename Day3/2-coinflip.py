import random

toss=input("Do you want to  toss the coin? (Y/N) ")
if (toss=="Y" or toss=="y"):
    result=random.randint(0,1)

    if(result==1):
        print("Heads")
    else:
        print("Tails")