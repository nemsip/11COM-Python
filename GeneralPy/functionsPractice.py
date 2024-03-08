# This is a program to practice your functions. For each problem, un-comment the function
# definition and the test line that calls it, then write the required function.
# Some comments actually ARE comments. Don't un-comment these...

def add_2_integers(number1, number2):
    # takes two integers as input, returns sum of the integers
    total = number1 + number2
    return total


def is_positive(the_number):
    # takes a single integer input, returns a boolean, true if positive, false otherwise
    if the_number > 0:
        return True
    else:
        return False


# def celsius_to_fahr(celsiusValue):
# takes a float celsius, converts to a float fahrenheit
# NOTE to convert a celsius temperature, MULTIPLY by 1.8 and THEN ADD 32

# def scream_word(the_word):
# returns uppercase version of the_word. Google how to do this in Python

# def is_in_range(the_value, min_allowed, max_allowed):
# Returns True if the_value is between min_allowed and max_allowed, otherwise returns False

# def print_sequence(first_term, difference, number_of_terms):
# creates a sequence of number_of_terms numbers, starting with the first_term, going up by
# difference each time.
# Output is to console, no value is returned

# def return_sequence(first_term, difference, number_of_terms):
# creates a sequence of number_of_terms numbers, starting with the first_term, going up by
# difference each time.
# returns a string with all the terms, separated by commas


# Test add_2_integers
print(add_2_integers(2, 2))  # Should output 4

# Test is_positive
print(is_positive(2))  # Should output True
print(is_positive(-2))  # Should output False

# Test scream_word
# print (scream_word("hello")) #Should output "HELLO"
# print (scream_word("How are you doing?")) #Should output "HOW ARE YOU DOING?"

# Test is_in_range
# print (is_in_range(3, 1, 10)) #Should output "True"
# print (is_in_range(12, 1, 10)) #Should output "False"
# print (is_in_range(10, 1, 10)) #Should output "True"
# print (is_in_range(-10, 1, 1000)) #Should output "False"

# Test celsius_to_fahr
# print (celsius_to_fahr(0)) #Should output 32
# print (celsius_to_fahr(17.5)) #Should output 63.5

# Test sequence functions
# print_sequence(2, 3, 5) #Should print 2, 5, 8, 11, 14
# print(return_sequence(2, 3, 5)) #Should print 2, 5, 8, 11, 14