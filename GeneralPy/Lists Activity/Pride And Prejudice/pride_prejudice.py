import os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def clean_text(text):
    text = text.lower()
    for character in "().,!?-_1234567890'\";:":
        text = text.replace(character, "")
    return text

def sixty_sixth_word(words):
    return words[65]

def count_words_starting_with_m(words):
    return sum(1 for word in words if word.startswith('m'))

def count_words(words):
    return len(words)

def count_words_ending_with_s(words):
    return sum(1 for word in words if word.endswith('s'))

def count_words_starting_with_vowel(words):
    return sum(1 for word in words if word[0] in 'aeiou')

def count_words_containing_her(words):
    return sum(1 for word in words if 'her' in word)

def most_common_word(words):
    return Counter(words).most_common(1)[0][0]

def last_double_letter_word(words):
    for word in reversed(words):
        if any(word.count(letter) >  1 for letter in word):
            return word
    return None

def count_words_with_double_letters(words):
    return sum(1 for word in words if any(word.count(letter) >  1 for letter in word))

with open("Pride_and_Prejudice.txt") as file:
    text = file.read()
    text = clean_text(text)
    words = text.split()

print(f"The  66th word is {sixty_sixth_word(words)}")
print(f"There're {count_words_starting_with_m(words)} words that start with 'm'")
print(f"The total number of words is {count_words(words)}")
print(f"There are {count_words_ending_with_s(words)} words that end with 's'")
print(f"There are {count_words_starting_with_vowel(words)} words that start with a vowel")
print(f"There are {count_words_containing_her(words)} words containing 'her'")
print(f"The most common word is {most_common_word(words)}")
print(f"The last word with a double letter is {last_double_letter_word(words)}")
print(f"There are {count_words_with_double_letters(words)} words with double letters")
