carrots = int(input('How many carrots do you have? '))
rabbits = 6
if rabbits > carrots:
    print('There are not enough carrots')
elif rabbits < carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')

# Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes. Let's write a
# program to help me to remember the right clothes.
# The program should check if the
# first item in the clothes list is "shorts" . If it is it should change
# the value to "warm coat" .

clothes = [
"shorts",
"shoes",
"t-shirt",
]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"
print(clothes)

# There are functions designed for lists
# len(): the number of items in a list
# max(): The biggest value in a list
# min(): The smallest value in a list

costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(max(costs))
print(min(costs))

# Functions for changing the order of a list
#
# sorted(): Sorts the
# reversed(): Reverses the order of a list

print(sorted(costs))
print(list(reversed(costs)))

# Exercise 4.2: Make a list of game scores. Using list functions write code to output information of the
# scores in the following format:
## Number of scores: 10
# Highest score: 200
# Lowest score: 3


game_scores = [20, 34, 3, 19, 200, 180, 38, 90, 88, 102]
number_of_scores = (len(game_scores))
lowest_score = (min(game_scores))
highest_score = (max(game_scores))

print(f"number_of_scores:{number_of_scores}")
print(f"highest score: {highest_score}")
print(f"lowest score: {lowest_score}")

# Extension: Output all of the scores in descending order
game_scores.sort(reverse=True)
print(game_scores)


