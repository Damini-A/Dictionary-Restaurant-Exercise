"""Restaurant rating lister."""


# put your code here

import sys

scores_file = sys.argv[1]

# for line in scores_file:
#    each_line = line.rstrip().split(":")
#    print(line)



# scores_file = open("scores.txt")

score_dict = {}

for line in open(scores_file):
    each_line = line.rstrip().split(":")

    score_dict[each_line[0]] = int(each_line[1])


restaurant_name = input("Please type a restaurant.").title()
restaurant_score = int(input("Please type a score."))
print ("****************************************")
print()
score_dict[restaurant_name] = restaurant_score


sorted_tuple = sorted(score_dict.items())

for line in sorted_tuple:
    print(f"{line[0]} is rated at {line[1]}.")

