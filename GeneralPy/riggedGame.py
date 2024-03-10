import random

total = 1

print("Welcome to the rigged game! Computer goes first.")
print("Computer chose 1")

while total < 100:

    while True:
        try:
            playerChoice = int(input("Choose a number between 1 and 10: "))
            if playerChoice <= 1 or playerChoice <= 10:
                break
            else:
                print("Invalid input. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 10.")


    print(f"Total so far: {total}")

    total += playerChoice
    if total >= 100:
        print("You win!")
        break

    # computerChoice = random.randint(1, 10)
    computerChoice = 11 - playerChoice
    total += computerChoice

    print(f"Computer chose {computerChoice}")
    print(f"Total so far: {total}")

    if total >= 100:
        print("Computer wins!")
        break
