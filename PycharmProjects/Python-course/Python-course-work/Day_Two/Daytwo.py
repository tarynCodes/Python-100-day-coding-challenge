#Data Types

#string
print("Hello"[4]) #subscripting
print("123" + "456") #concatination

#interger - whole numbers
print(123 + 456)
123_345_678 #visualize large numbers

#float - decimal numbers
3.14159

#boolean - test true or false
True
False

# num_char = len(input("what is your name?")) #currently an int
# new_num_char = str(num_char) #change to a string
# print("your name has " + new_num_char + " characters!")

a = float(123)
print(type(a)) #can use type function to find out the datatype we are working with



#challenge - split the string and total up the sum of the two numbers
two_digit_number = "34"

# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
total = first_digit + second_digit
print(total)

