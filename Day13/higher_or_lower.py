import random
import os
from ascii_art import logo, vs
from game_data import data

def printing_data(data, a_or_b):
    print(f"{a_or_b}: {data['name']}, {data['description']}, {data['country']}")

def game(score):
    data1=(random.choice(data))
    data2=data1
    while data1==data2:
        data2=random.choice(data)

    printing_data(data1, "Compare A")
    print(vs)
    printing_data(data2, "Against B")

    answer=input("\n Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls || clear')
    print(logo)
        
    if data1['follower_count']>data2['follower_count'] and answer=="a":
        score+=1
        print(f"You're right! Current score: {score} \n")
        game(score)
    elif data1['follower_count']<data2['follower_count'] and answer=="b":
        score+=1
        print(f"You're right! Current score: {score} \n")
        game(score)
    else:
        print(f"Sorry, that's wrong. Final score: {score} \n")
        return

score=0
print(logo)
game(score)

# TODO:
# a func to print data of two randoms
# another func to 
