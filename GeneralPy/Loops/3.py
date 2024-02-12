# Write a program which will allow the user to input a first number, last number and 'step' size, and then print out all of the numbers from first to last with the proper step size.

first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
step = int(input("Enter the step size: "))

for i in range(first, last + 1, step):
    print(i, end=' ')

