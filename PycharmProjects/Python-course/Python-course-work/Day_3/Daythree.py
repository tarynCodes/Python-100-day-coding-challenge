# conditional statements

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride :( ")

# comparison statements

# > greater than
# < less than
# >= equal to or greater than
# =< equal to or less than
# == values are equal on both sides
# != values are not equal

# Which number do you want to check?
number = int(input("What is your chosen number?"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# # Write your code below this line 👇

# nested statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7")
    elif 45 <= age <= 55:
        print("Have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are £12")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is £{bill}")
else:
    print("Sorry, you have to grow taller before you can ride :( ")


# BMI calculator using conditional statements
height = float(input("What is your height in metres?"))
weight = int(input("What is your weight?"))
bmi = weight / (height * height)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Leap year challenge
year = int(input("Which year would you like to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Pizza Order
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")


# love calculator
print("The Love Calculator is calculating your score...")
name1 = input("what is your name?")
name2 = input("What is their name?")

lowercase_name_1 = name1.lower()
lowercase_name_2 = name2.lower()
lowercase_names = lowercase_name_1 + lowercase_name_2

T = lowercase_names.count("t")
R = lowercase_names.count("r")
U = lowercase_names.count("u")
E = lowercase_names.count("e")
true_score = T + R + U + E

L = lowercase_names.count("l")
O = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
love_score = L + O + v + e

true_love_score = str(true_score) + str(love_score)
total = int(true_love_score)

if total < 10 or total > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif 40 < total < 50:
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}.")

