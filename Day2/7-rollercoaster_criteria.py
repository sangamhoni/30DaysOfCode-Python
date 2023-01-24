# WAP to check if a user can ride a rollercoaster or not

print("Welcome to the Rollercoaster")
height=int(input("What's your height? (in cm) "))
bill=0

if height >=120:
    print("You can ride the rollercaster")

    age=int(input("How old are you? "))
    if(age<12):
        bill=5
    elif (age<=18):
        bill=7
    else:
        bill=12
        # print("Please pay $12 for the rollercoaster.")
    
    photo=input("Do you want a photo to be taken ($3)? Y/N: ")
    if(photo=="Y" or photo=="y"):
        bill += 3
    print(f"Please pay ${bill} for the rollercoaster.")

else:
    print("Sorry, you're too short to be in a rollercoaster")