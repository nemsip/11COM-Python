# Write a simple python program with for loops to calculate the average of a cricket player’s scores. The program should input scores, add them up and count how many there are. When a score of 1000 is entered (don’t include this in the scores!), the program will stop and print out a statement like:
# There were ___ scores entered. The total score is ___ giving an average score of ___.

total_score = 0
count = 0

while True:
    score = int(input("Enter a score (enter  1000 to stop): "))
    if score == 1000:
        break
    total_score += score
    count += 1

average_score = total_score / count if count > 0 else 0

print("There were {} scores entered. The total score is {} giving an average score of {}.".format(count, total_score, average_score))
