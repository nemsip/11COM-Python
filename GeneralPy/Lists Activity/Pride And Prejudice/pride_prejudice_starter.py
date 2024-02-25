
# Functions and lists practice
import os

# Make sure Python is running in the current directory and not somewhere else.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Remove numbers and punctuation from some text and change it to lowercase.
def clean_text(text):
    text = text.lower()
    for character in "().,!?-_1234567890'\";:":
        text = text.replace(character, "")
    return text

def sixty_sixth_word(words):
    word = "THE ANSWER" # TO DO: Change this.
    return word

def count_words_starting_with_m(words):
    count = 0
    # TO DO: Count the words starting with 'm'.
    return count

with open("Pride_and_Prejudice.txt") as file:
    text = file.read()
    text = clean_text(text)

    # Split into a list of words
    words = text.split()
    print(words)

answer = sixty_sixth_word(words)
print(f"The sixty sixth word is {answer}")

answer = count_words_starting_with_m(words)
print(f"There are {answer} words that start wth m")
