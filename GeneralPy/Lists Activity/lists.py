
scores = [402,  498,  852,  720,  688,  378,  303,  219,  521,  940,  517,  725,  714,  768,  299,  555,  888,  362,  416,  938,  767,  709,  596,  1000,  854,  838,  751,  143,  775,  435,  173,  122,  713,  240,  1020,  270,  651,  923,  620,  277,  214,  720,  479,  42,  289,  255,  749,  221,  453,  584,  789,  168,  486,  629,  122,  725,  835,  270,  903,  896,  1007,  209,  993,  385,  286,  558,  1043,  589,  458,  666,  767,  547,  279,  376,  208,  213,  130,  66,  981,  887,  339,  236,  542,  285,  394,  709,  539,  360,  680,  378,  321,  318,  977,  955,  432,  360,  813,  673,  1026,  394]

# How many numbers in the list?
num_scores = len(scores)
print(f"There are {num_scores} numbers in the list.")

# What's the largest number in the list?
largest_number = max(scores)
print(f"The largest number in the list is {largest_number}.")

# What's the smallest number in the list?
smallest_number = min(scores)
print(f"The smallest number in the list is {smallest_number}.")

# What's the  23rd number in the list?
twenty_third_number = scores[22]
print(f"The  23rd number in the list is {twenty_third_number}.")

# What's the last number in the list?
last_number = scores[-1]
print(f"The last number in the list is {last_number}.")

# What's the second lorgest number in the list?
scores_sorted = sorted(scores, reverse=True)
second_largest_number = scores_sorted[1]
print(f"The second largest number in the list is {second_largest_number}.")

# What's the sum of all the numbers in the list?
sum_scores = sum(scores)
print(f"The sum of all the numbers in the list is {sum_scores}.")

# What's the mean (average - add them up and divide by how many there are)?
mean_score = sum_scores / num_scores
print(f"The mean of the numbers in the list is {mean_score}.")

# What's the median of the numbers?
scores_sorted = sorted(scores)
if num_scores % 2 == 0:
    median_score = (scores_sorted[num_scores // 2 - 1] + scores_sorted[num_scores //  2]) /  2
else:
    median_score = scores_sorted[num_scores // 2]
print(f"The median of the numbers in the list is {median_score}.")

# Which number occurs the most often? (if there is a tie, list them all)
from collections import Counter
score_counts = Counter(scores)
max_count = max(score_counts.values())
most_common_numbers = [score for score, count in score_counts.items() if count == max_count]
print(f"The most common number(s) in the list is/are {most_common_numbers}.")

# Print a list of all the numbers that occur only once, sorted smallest to largest
unique_scores = [score for score in scores if scores.count(score) == 1]
unique_scores.sort()
print(f"Numbers that occur only once, sorted smallest to largest: {unique_scores}")

# Which number occurs the second most often?  (if there is a tie, paste them all)
score_counts_sorted = sorted(score_counts.items(), key=lambda x: x[1], reverse=True)
second_max_count = score_counts_sorted[1][1] if len(score_counts_sorted) > 1 else None
second_most_common_numbers = [score for score, count in score_counts_sorted if count == second_max_count]
print(f"The second most common number(s) in the list is/are {second_most_common_numbers}.")

























