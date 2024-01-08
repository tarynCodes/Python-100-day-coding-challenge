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

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay £5")
    elif age <= 18:
        print("Please pay £7")
    else:
        print("Please pay £12")
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
