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

#################################################################################
# Nesting
# {key: [list], key: {dict}}
capitals = {
        "France": "Paris",
        "Germany": "Berlin"
        }

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_pretzels": 25}
    }

print(travel_log["France"]["cities_visited"])

# Nesting a dictionary in a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 25
    }
    ]

# challenge add new country as a dictionary to travel_log list

country = input("Add country name")
visits = int(input("Number of visits"))
list_of_cities = eval(input("list the cities you've been to"))

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


def add_new_country(name=country, time_visited=visits, cities_visited=list_of_cities):
    new_country = {
                "country": name,
                "visits": time_visited,
                "cities": cities_visited
                }
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")