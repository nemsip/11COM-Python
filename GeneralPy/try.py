
success = False
while not success:
    try:
        responce = int(input("Choose a number between 1 and 100 >_ "))
        if responce > 100:
            print("That's too high.")
        elif responce < 1:
            print("That's too low.")
        else:
            print("Your number is " + str(responce) + ".")
            success = True
    except ValueError:
        print("Invalid input")