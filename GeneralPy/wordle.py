import random
import csv

emoji_mapping = {
    'correct': '🟩',
    'in_word': '🟨',
    'incorrect': '⬛'
}

def load_words_from_csv_pls_work(filename, word_column_index):
    words = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)   
        for row in reader:
            words.append(row[word_column_index])
    return words

word_list = load_words_from_csv_pls_work(r'C:\Users\nemit\Documents\11COM\Python\GeneralPy\fiveletterwords.csv',0)

while True:
    answer = random.choice(word_list).upper()
    print(answer)
    attempts = 6

    while attempts > 0:
        guess = input("Enter your guess: ").upper()

        if len(guess) != 5:
            print("Please enter a   5-letter word.")
            continue

        result = []
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                result.append(emoji_mapping['correct'])
            elif guess[i] in answer:
                result.append(emoji_mapping['in_word'])
            else:
                result.append(emoji_mapping['incorrect'])

        print(" ".join(result))

        if guess == answer:
            print("\nCongratulations! You guessed the word correctly!")
            break

        attempts -= 1
        print(f"\nAttempts remaining: {attempts}\n")

    if attempts == 0:
        print("You ran out of turns!\nThe word was: '" + str(answer) + "'")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again.lower() != "yes":
        break
