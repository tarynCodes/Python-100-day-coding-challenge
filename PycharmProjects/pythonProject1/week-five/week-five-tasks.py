# How do I output the species values for each of the dictionaries?

# species_array = [
#
# {'species': 'zebra', 'name': 'Penelope'},
#
# {'species': 'penguin', 'name': 'Jenn'},
#
# {'species': 'elephant', 'name': 'Harris'},
#
# {'species': 'flamingo', 'name': 'Florence'},
#
# ]
#
# for animals in range(len(species_array)):
#     print(species_array[animals]['species'])

# Exercise 5.1: Create a to-do list program that writes user input to a file

# The program should:
# Ask the user to input a new to-do item
# Read the contents of the existing to-do items
# Add the new to do item to the existing to-do items
# Save the updated to-do items
# You will need to manually create a new file called todo.txt in the same folder as your program before you
# start
# new_item = input('Enter a task for your todo list: ')
# with open('todo.txt', 'r') as text_file: #read file
#     todo = text_file.read()
# todo += new_item + '\n'
# with open('todo.txt', 'w') as text_file:
#     text_file.write(todo)


import csv

field_names = ['name', 'age']

data = [

{'name': 'Jill', 'age': 32},

{'name': 'Sara', 'age': 28},

{'name': 'Louis', 'age': 21},

]

with open('team.csv', 'w+') as csv_file:

    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()

    spreadsheet.writerows(data)

# Exercise 5.2: This program is supposed to read data about trees from a file to find the shortest tree. Complete
#
# the program adding code to open trees.csv .
#
# The trees.csv file included with your student guides. Save the csv file in the same folder as your Python
#
# program.

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

    shortest_height = min(heights)

print(shortest_height)

