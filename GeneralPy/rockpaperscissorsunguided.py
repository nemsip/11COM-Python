import random
import time

choices = ['rock', 'paper', 'scissors']

def winner_chicken_dinner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'paper' and computer == 'rock') or \
            (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
    print(winner_chicken_dinner(user_choice, computer_choice))

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    while play_again != "yes" and play_again != "no":
        print("That is not a valid option! Please choose either 'yes' or 'no'.")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "no":
        print("Okay, exiting the program in five seconds...")
        time.sleep(5)
        exit()