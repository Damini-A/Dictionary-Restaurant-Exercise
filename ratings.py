"""Restaurant rating lister."""


# put your code here

import sys
from random import choice

scores_file = sys.argv[1]

# for line in scores_file:
#    each_line = line.rstrip().split(":")
#    print(line)



# scores_file = open("scores.txt")

score_dict = {}

for line in open(scores_file):
    each_line = line.rstrip().split(":")

    score_dict[each_line[0]] = int(each_line[1])


while True:
    # This code is if the user wants to see restaurants and ratings.
    choice = input("Please enter: 's' to see all ratings, 'a' to add a restaurant/rating, 'u' to update, or 'q' to quit :-")
    
    if choice == "s":
        
        sorted_tuple = sorted(score_dict.items())

        for line in sorted_tuple:
            print(f"{line[0]} is rated at {line[1]}.")
        print()

    elif choice == "a":
# This code is if the user wants to add a new restaurant and rating.
        restaurant_name = input("Please type a restaurant.").title()
        restaurant_score = int(input("Please type a score."))

        while restaurant_score > 5 or restaurant_score < 1:
            restaurant_score = int(input("Please enter a score between 1 and 5."))

        print ("****************************************")
        print()

        score_dict[restaurant_name] = restaurant_score

        sorted_tuple = sorted(score_dict.items())

        for line in sorted_tuple:
            print(f"{line[0]} is rated at {line[1]}.")
        print()

    elif choice == "u":
        random_restaurant = choice(sorted_tuple)
        print(random_restaurant)


    elif choice == "q":
        sys.exit()

    else :
        print("invalid input")
        continue




