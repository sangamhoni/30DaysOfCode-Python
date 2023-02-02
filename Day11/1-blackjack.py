# guide:
# you get 2 cards
# computer gets 2 cards (only one is visible to you)
# every king queen jack is considered a 10
# Ace can be counted either as 1 or 11, whatever you wish
# you try to bring your cards sum to as close as 21, if it exceeds you lose immediately
# if the dealers card is less than 17, he has to take another card
# If yours and dealers is equal, its a draw
import random
import os
from blackjack_logo import logo

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_again():
    play_more=input("\n Do you want to play Blackjack? (Y/N): ").lower()
    if play_more=='y':
        os.system('cls || clear')
        play_game()
    else:
        exit()


def play_game():
    print(logo)
    user_cards=random.choices(cards, k=2)
    computer_cards=random.choices(cards, k=2)

    user_sum=sum(user_cards)
    computer_sum=sum(computer_cards)

    print(f"    Your cards: {user_cards}, Current score: {user_sum}")
    print(f"    Computer's first card: {computer_cards[0]}")

    if (computer_sum==21):
        if (user_sum==21):
            print(f"    Computer's second card: {computer_cards[1]}")
            print("\n Draw! The computer also got a Blackjack")
            # play_again=input("Do you want to play Blackjack? (Y/N): ").lower()
            # if play_again=='y':
            #     os.system('cls')
            #     play_game()
            play_again()
        else:
            print(f"    Computer's second card: {computer_cards[1]}")
            print("\n Computer won with a Blackjack!")
            # play_again=input("Do you want to play Blackjack? (Y/N): ").lower()
            # if play_again=='y':
            #     os.system('cls')
            #     play_game()
            play_again()

    elif (user_sum==21):
        print(f"    Computer's second card: {computer_cards[1]}")
        print("\n You won with a Blackjack!")
        # play_again=input("Do you want to play Blackjack? (Y/N): ").lower()
        # if play_again=='y':
        #     os.system('cls')
        #     play_game()
        play_again()


    user_draw=False
    another_card='y'

    while another_card=='y':
        if (user_sum>21):
            if 11 in user_cards:
                user_cards[user_cards.index(11)]=1
                user_sum=sum(user_cards)
            else:
                print(f"    Your cards: {user_cards}, Current score: {user_sum}")
                print("\n You went over. You lose!")
                play_again()
        if user_draw:
            print(f"    Your cards: {user_cards}, Current score: {user_sum}")
        another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card=='y':
            user_draw=True
            user_cards.append(random.choice(cards))
            # print((user_cards))
            # print(sum(user_cards))
            user_sum=sum(user_cards)
        else:
            while (computer_sum<17):
                computer_cards.append(random.choice(cards))
                computer_sum=sum(computer_cards)
                if (computer_sum>21):
                    if 11 in computer_cards:
                        computer_cards[computer_cards.index(11)]=1
                        computer_sum=sum(computer_cards)
                    else:
                        print(f"    Computer cards: {computer_cards}, Current score: {computer_sum}")
                        print("\n Computer went over. You win!")
                        play_again()
            
            print(f"    Your final hand: {user_cards}, final score: {user_sum}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_sum}")
            
            if user_sum==computer_sum:
                print("\n Draw!")
            elif user_sum > computer_sum:
                print("\n You won!")
            else:
                print("\n Computer won!")
            
            play_again()

play_game()