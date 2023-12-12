import math

#session1

#penelope needs to be in a string - originally was without quotations
my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#change chair amount to integer
#print statement to just print message
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'You need to buy {} nails'.format(total_nails)
print(message)

#I have a lot of boxes of eggs in my fridge
#and I want to calculate how many omelettes I can make.
#Write a program to calculate this.
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
#but I should be able to easily change these values if I want. The output should say something like
#"You can make 9 omelettes with 6 boxes of eggs".

my_egg_boxes = 112
my_eggs = my_egg_boxes * 6
omelette = math.floor(my_eggs / 4)
message = f'You can make {omelette} omelettes with {my_egg_boxes} boxes of eggs'
print(message);

##################################################################################################################

