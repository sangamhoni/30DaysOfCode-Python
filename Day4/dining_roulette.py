# WAP to choose a random person from a gorup to pay the bills

import random
names=input("Tell me everybody's name separate by a comma: ")
name_list=names.split(", ")
total=len(name_list)
chosen_person=name_list[random.randint(0, total-1)]

# or just do: chosen_person=random.choice(name_list)

print(f"{chosen_person} is going to pay the bills this time")