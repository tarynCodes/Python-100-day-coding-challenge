import random
# import another file
import module

# Produce a random number between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)
print(module.pi)

# # 0.00000 - 0.999999...
random_float = random.random()
print(random_float)

#  random float numbers between 0.00000 - 4.9999999
random_float_5 = random_float * 5
print(random_float_5)

# # Heads or Tails game
random_int = random.randint(0, 1)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

# Lists - like arrays
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# alter the list item
states_of_america[1] = "New York"
# add a new item to the end of list
states_of_america.append("TarynLand")
# extend the list by more than one
states_of_america.extend(["Delaware", "Alanta", "Texas"])
# first in list
print(states_of_america[0])
# last in list
print(states_of_america[-1])
# print length of list
print(len(states_of_america))

fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Map challenge
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")
if position == "A1":
    map[0][0] = "X"
elif position == "A2":
    map[1][0] = "X"
elif position == "A3":
    map[2][0] = "X"
elif position == "B1":
    map[0][1] = "X"
elif position == "B2":
    map[1][1] = "X"
elif position == "B3":
    map[2][1] = "X"
elif position == "C1":
    map[0][2] = "X"
elif position == "C2":
    map[1][2] = "X"
elif position == "C3":
    map[2][2] = "X"

print(f"{line1}\n{line2}\n{line3}")

# Another way of solving
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")
# Gets the first letter of the position (A, B, or C) and converts it to lowercase.
letter = position[0].lower()
# Represents the letters A, B, C.
abc = ["a", "b", "c"]
# Finds the index (position) of the chosen letter in the list abc.
letter_index = abc.index(letter)
# Gets the second character of the position (the number) and subtracts 1 to get the index.
number_index = int(position[1]) - 1
# Puts the "X" (treasure) at the chosen position on the map.
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
