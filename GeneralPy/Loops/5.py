# Write a program which will let the user input 12 numbers, add them up and print out the total

total = 0

for i in range(12):
    number = int(input("Enter number {}: ".format(i + 1)))
    total += number

print("The to tal is:", str(total) + f"\n🔥🔥🔥")
