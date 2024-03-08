# This is the 100 Game by Reverend Charles Lutwidge Dodgson, features in Alice in Wonderland. Make it so this game is unbeatable. The computer should always win. Use Arithmatic sequencing to make the computer win.

def play_game():
    total = 0
    while total < 100:
        user_choice = int(input("Enter a number between 1 and 10: "))
        
        if user_choice < 1 or user_choice > 10:
            print("Invalid input. Please choose a number between 1 and 10.")
            continue
        
        total += user_choice

        if total >= 100:
            print("Sorry, the computer won! (Not rigged fr)")
            break
        
        computer_choice = 11 - user_choice
        
        if total + computer_choice >= 100:
            computer_choice = 100 - total
        
        total += computer_choice

        print("Total:", total)
        
        print("Computer chooses:", computer_choice)
        
        if total >= 100:
            print("Sorry, the computer won! (Not rigged fr)")
            break

play_game()