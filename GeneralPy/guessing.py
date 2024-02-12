import random
import time

print("""
  ____  __ __    ___  _____ _____ ____  ____    ____       ____   ____  ___ ___    ___ 
 /    ||  |  |  /  _]/ ___// ___/|    ||    \  /    |     /    | /    ||   |   |  /  _]
|   __||  |  | /  [_(   \_(   \_  |  | |  _  ||   __|    |   __||  o  || _   _ | /  [_ 
|  |  ||  |  ||    _]\__  |\__  | |  | |  |  ||  |  |    |  |  ||     ||  \_/  ||    _]
|  |_ ||  :  ||   [_ /  \ |/  \ | |  | |  |  ||  |_ |    |  |_ ||  _  ||   |   ||   [_ 
|     ||     ||     |\    |\    | |  | |  |  ||     |    |     ||  |  ||   |   ||     |
|___,_| \__,_||_____| \___| \___||____||__|__||___,_|    |___,_||__|__||___|___||_____|
                                                                                                                     
                                          (v2.0.4)
""")

ans = random.randint(1, 100)
print(ans)
guesses = 0

response = int(input("Choose a number between 1 and 100 >_ "))

while response != ans:
    if ans == response
        guesses += 1
        print("Correct! You win! The answer was " + ans + "!")
        print("It's taken " + str(guesses) + "guesses to get it!")
        continue
    elif response > ans:
        print("Too high! Try a lower number")
    else:
        print("Too low! Try a higher number")
    response = int(input("Choose a number between 1 and 100 >_ "))

again = str(input("Do want to play again?\n1. Yes\n2. No\n>_ ")).lower
while again not in ["1", "2"]:
    print("Sorry, that is not a valid answer. Try again.")
    again = str(input("Do want to play again?\n1. Yes\n2. No\n>_ ")).lower
    if again == "1":
        continue
    elif again == "2":
        print("Alright, we hope you enjoy this game!\nThe game will exit in 5 seconds.")
        time.sleep(5)