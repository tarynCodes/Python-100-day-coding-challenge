import random

# Comparisons amd Logical Operators

# print ('~' * 0) up to nine
for number in range(9):
    print('~' * number)

# Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
#
# 1. Input the price of a burger using input()
#
# 2. Check whether the price is less than or equal ( <= ) 10.00
#
# 3. Print the result in the format below
#
# Burger is within budget: True
#
# Hint: remember to convert the input from a string to a decimal with float()
# Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian
# option The output should say whether the cost is within budget AND has a vegetarian option
# Restaurant meets criteria: True
# burger_price = input('How much does the burger cost at this restaurant?')
# is_affordable = float(burger_price) <= 10
#
# vegetarian_options = input('Does this restaurant have veg options? (y/n)')
# has_veg_options = vegetarian_options == 'y'
#
# should_go_to_restaurant = is_affordable and has_veg_options
# print(f'Burger is within budget and has veg options: {should_go_to_restaurant}')


# Exercise 3.3: Rewrite the output of your burger program to use if statements
# If it is a good choice it should be:
# This restaurant is a great choice!
# If it is not a good choice it should be:
# Probably not a good idea

burger_price = input('How much does the burger cost at this restaurant?')
is_affordable = float(burger_price) <= 10

vegetarian_options = input('Does this restaurant have veg options? (y/n)')
has_veg_options = vegetarian_options == 'y'

good_choice = is_affordable and has_veg_options
if good_choice:
    print('This restaurant is a great choice!')
else:
    print('Probably not a good idea')

# Exercise 3.4: Now that you've finished your burger, you want to pay for your food. Let's write a program to
# calculate your meal and apply a discount if applicable.
# If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. The program
# should print "Discount applied" or "No discount" depending on whether the discount criteria was met.

total_cost = float(input('what was the cost of your meal?'))
discount = input('do you have a discount? (y/n)')
is_discount = discount == 'y'
meal_over_twenty = total_cost >= 20.00
discount_applicable = is_discount and meal_over_twenty

if discount_applicable:
    total_cost = (total_cost * 0.9)
    print('discount applied')
    print(f'your total is {total_cost}')
#
# else:
#     print('no discount this time!')
#     print(f'Your total is: {total_cost}')

# temp = int(input('enter the temp: '))
#
if temp > 200:
    print("the oven is too hot")
elif temp < 180:
    print("the oven is too cold")
elif temp == 180:
    print("the oven is the correct temp")


# Exercise 3.6: This program uses random to simulate a coin flip.
# To finish the program you will need to add the following:
# If the random coin flip matches the choice input by the user then they win
# Otherwise if the random coin flip does not match the choice input by the user then they lose
# In [ ]:
# import random
# def flip_coin():
# random_number = random.randint(1, 2)
# if random_number == 1:
# side = 'heads'
# else:
# side = 'tails'
# return side
# choice = input('heads or tails: ')
# result = flip_coin()
# print('The coin landed on {}'.format(result))

def coinflip():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
        return side
    else:
        side = 'tails'
        return side


choice = input('heads or tails: ')
result = coinflip()
if choice == result:
    print(f'You win, the coin landed on {result}!')
else:
    print(f'sorry you lose, the coin landed on {result}!')
