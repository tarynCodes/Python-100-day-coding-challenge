# Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
# Prints all fruit in list

# Average height challenge

student_heights = input("Input a Python list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
number_of_students = 0
for student in student_heights:
    number_of_students += 1
    total_height += student
average_height = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")

# Largest score finder
student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

largest_score = student_scores[0]
for student in student_scores:
  if student > largest_score:
    largest_score = student

print(f"The highest score in the class is: {largest_score}")

# range function - generate a range of numbers to loop through
count = 0
for number in range(1, 101, 3):  # last digit is a step
    count += number
print(count)

# sum of numbers using range function
target = int(input("Enter a number between 0 and 1000"))
final_digit = target + 1
count = 0
for number in range(0, final_digit, 2):
    count += number
print(count)

# fizzBuzz challenge
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)