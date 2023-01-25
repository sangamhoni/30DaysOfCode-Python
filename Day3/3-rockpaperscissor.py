import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

line='''
=======================================================================================
'''

you_won='''_   _ ____ _  _    _ _ _ ____ _  _ 
 \_/  |  | |  |    | | | |  | |\ | 
  |   |__| |__|    |_|_| |__| | \|
  '''

computer_won='''____ ____ _  _ ___  _  _ ___ ____ ____    _ _ _ ____ _  _ 
|    |  | |\/| |__] |  |  |  |___ |__/    | | | |  | |\ | 
|___ |__| |  | |    |__|  |  |___ |  \    |_|_| |__| | \|
'''

draw='''___  ____ ____ _ _ _ 
|  \ |__/ |__| | | | 
|__/ |  \ |  | |_|_|
'''


print('''
 ___  ___   ___ _  __     ___  _   ___ ___ ___     ___  ___ ___ ___ ___  ___  ___  ___ 
| _ \/ _ \ / __| |/ /    | _ \/_\ | _ \ __| _ \   / __|/ __|_ _/ __/ __|/ _ \| _ \/ __|
|   / (_) | (__| ' <     |  _/ _ \|  _/ _||   /   \__ \ (__ | |\__ \__ \ (_) |   /\___\\
|_|_\\\___/ \___|_|\_\    |_|/_/ \_\_| |___|_|_\   |___/\___|___|___/___/\___/|_|_\|___/''')

print(f'''
{line}
What do you choose?
    1 - Rock
    2 - Paper
    3 - Scissor
''')
user=input("")
try:
    user=int(user)
except ValueError:
    #nothing
    print("Enter either 1, 2 or 3")

print(line)
if(user==1):
    print("You chose ROCK")
    print(rock)
elif (user==2):
    print("You chose PAPER")
    print(paper)
else:
    print("You chose SCISSORS")
    print(scissors)

print(line)

computer=random.randint(1,3)
if(computer==1):
    print("Computer chose ROCK")
    print(rock)
elif (computer==2):
    print("Computer chose PAPER")
    print(paper)
else:
    print("Computer chose SCISSORS")
    print(scissors)

print(line)

if(user==computer):
    print(draw)
elif (user>computer):
    if(user!=3):
        print(you_won)
else:
    print(computer_won)
    
