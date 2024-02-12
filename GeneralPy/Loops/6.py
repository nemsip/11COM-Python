# Write a program to input a number, then add up all the numbers from 1 to this number. (These are called triangular numbers.) The program should print out a message like:
# Adding up all the numbers from 1 to ___ gives ___.

number = int(input("Enter a number: "))

sum = 0

for i in range(1, number + 1):
    sum += i

print("Adding up all the numbers from  1 to {} gives {}. Absolutely wicked bruv.".format(number, sum))
