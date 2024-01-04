#Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')

# Answer part 4. Extra ( in print function removed.
# print(("New lines can be created with a backslash and n.")
print("New lines can be created with a backslash and n.")


# Provide any name in the input pane below.
# That value can be accessed using the input() function.
# Don't put anything inside the input() function!
numberOfLettersInName = input("What is your name?")
print(f"The number of letters in your name is: {len(numberOfLettersInName)}")


# switch variables
# There are two variables, a and b from input
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
temp = a
a = b
b = temp

# 🚨 Don't change the code below 👇
print("a:", a)
print("b:", b)
