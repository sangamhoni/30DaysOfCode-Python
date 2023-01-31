import os 
from logo import logo

print(logo)
print("Welcome to the secret auction")

auction={}
add_more=True
max_bid=0
max_bidder=''

while (add_more==True):
    name=input("What is your name: ")
    bid=int(input("What's your bid: $"))
    auction[name]=bid


    more_data=input("Are there any more bidders? (Yes/No): ").lower()
    
    if(more_data=="yes"):
        add_more=True
        os.system('cls')
        print(logo)
    else:
        add_more=False        
        
        for bidder in auction:
            if auction[bidder]>max_bid:
                max_bidder=bidder
                max_bid=auction[bidder]
        
        print(f"The winner is {max_bidder} with a bid of ${auction[max_bidder]}.")
