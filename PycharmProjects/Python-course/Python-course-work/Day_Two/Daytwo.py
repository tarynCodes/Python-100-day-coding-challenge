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


#mathematical operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3 # to the power of

print(3 * 3 / 3 + 3 - 3) #BIMDAS


#Challenge BMI calculator
# 1st input: enter height in meters e.g: 1.65
height = 1.65
# 2nd input: enter weight in kilograms e.g: 72
weight = 72
# 🚨 Don't change the code above 👆
height_bmi = float(height) * float(height)
bmi = int(weight) / height_bmi
int_bmi = int(bmi)
print(int_bmi)

#number manipulation
print(round(2.666666, 2)) #round -> round up, the second 2 is the how many decimal places
print(8 // 3) #floor -> change to a whole number round down
score = 0
score += 1 #will add one to score
print(score)
print(f"your score is {score}") #f strings are good for printing all datatypes
