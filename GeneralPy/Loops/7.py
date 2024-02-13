# Write a simple python program with for loops to calculate factorials. 6 factorial (written as 6!) is calculated as 6 x 5 x 4 x 3 x 2 x 1.

def factorial_thing(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

number = int(input("Enter a number: "))

factx = factorial_thing(number)

print("The factorial of {} is {}. \nBrilliant mate.".format(number, factx))
