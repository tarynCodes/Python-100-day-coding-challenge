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
# 🚨 Don't change the code above 👆
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
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
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
