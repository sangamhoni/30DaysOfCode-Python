import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

import os
# os.system('cls||clear')
chosen_word=random.choice(word_list)

answers=[]
for underscore in chosen_word:
    answers+="_"

score=0
lives=7
result=''
stored_inputs=[]
message=''

while (score != len(chosen_word)) and (lives>0):    

    print(logo)
    print(stages[lives])
    # print(chosen_word)
    print(f"{result}\n")
    print(f"{' '.join(answers)}")
    print('')
    guess=input("Guess the letter: ")
    guess=guess.lower()

    os.system('cls||clear')

    if guess in stored_inputs:
        result=f"You've already guessed {guess}"
    elif len(guess)!=1:
        result="Only one letter at a time!"
    else:
        stored_inputs+=guess
        
        if guess in chosen_word:
            for n in range(0, len(chosen_word)):
                if (guess==chosen_word[n]):
                    answers[n]=guess
                    score+=1
                    result=''
            
            if score == len(chosen_word):
                message="Congratulations! You won"
                
        else:
            result=f"{guess} is not in the word. You lose a life"
            lives-=1
            
            if lives==0:
                message=f"You lose! The word was {chosen_word}"
                # break

print(logo)
print(stages[lives])
print(f"{' '.join(answers)}\n")
print(message)
print("Thanks for playing\n")
