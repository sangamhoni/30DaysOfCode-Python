import random 
from logo_numberguess import logo

def guesser(answer, attempt):
    for i in range(attempt):
        print(f"\n You have {attempt-i} attempts remaining to guess the number.")
        guess=input("Make a guess: ")
        guess=int(guess)
        if (guess!=answer):
            if (guess>answer):
                print("Too high")
            else:
                print("Too low")
            print("Guess again.")
        else:
            print(f"You got it! The answer is {guess}.")
            return True
    
    print("\n You have run out of guesses, you lose.")
    return False

print(logo)
print("Welcome to the Number guessing game")
print("I am thinking of a number from 1 to 100.")
guessed_number = random.randint(1, 100)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty=='easy':
    guesser(guessed_number, 10)
elif difficulty=='hard':
    guesser(guessed_number, 5)



