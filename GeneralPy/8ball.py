import random
import time
responses = [
    "Yes",
    "Certainly",
    "Nope",
    "Maybe",
    "Definatly not!",
    "Ask again later"
]
print("Welcome to Magic 8 Ball!")

while True:
    question = input("Ask me a question: ").lower()
    answer = random.choice(responses)
    print(answer)

    response = input("Shake again? (y/n) ").lower()
    if response == "y":
        continue
    elif response == "n":
        print("Ok, I hope you enjoyed the game!\nThe program will close in 5 seconds.")
        time.sleep(5)
        break
    else:
        print("Invalid input.")
