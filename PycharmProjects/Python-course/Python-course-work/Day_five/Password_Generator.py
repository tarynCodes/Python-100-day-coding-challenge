#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# create a loop for letter
# loop through numbers
# loop through symbols
# pull out required number of each using random.choice
# randomise the password - random.shuffle

# Easy version - non shuffled

password = ""

for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password = password + random_letter

for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password = password + random_number

for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password = password + random_symbol


print(password)

# hard version - shuffled

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)


for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)


for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")


