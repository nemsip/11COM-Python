# calculator.py

import time

time.sleep(1)

while True:
    try:
        num = int(input("What number? >_ "))
        num2 = int(input("What the other number? >_ "))
        operation = int(input(f"What do you want to do with these two numbers?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n>_ "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if not 1 <= operation <= 4:
        print("Invalid input. Please choose a number between 1 and 4.")
        continue

    time.sleep(3)

    if operation == 1:
        print(num + num2)
    elif operation == 2:
        print(num - num2)
    elif operation == 3:
        print(num * num2)
    elif operation == 4:
        if num2 == 0:
            print("Invalid input. Division by zero is not possible.")
        else:
            print(num / num2)