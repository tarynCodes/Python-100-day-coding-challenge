# Dictionaries
# {Key: Value} pairs

programming_dictionary = {"Bug": "An error in a program that prevents "
                                 "the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          }
# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding an item to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # print keys
    print(key)
    # print values
    print(programming_dictionary[key])

# Printing students grades challenge
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 :
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


