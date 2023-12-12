#Inputs
import math
import datetime

pet = input('what kind of pet do you have?')
pets_name = input('what is your pets name?')
print(f'I have a {pet} named {pets_name}')

food = input('what is your favourite food?')
print(f'My favourite food is {food}')

purchased_pineapples = input('How many pineapples did you buy?')
total_pineapples = int(purchased_pineapples) + 10
print(total_pineapples)

friends = input('How many friends at your house?')
total_pizza = math.ceil(int(friends) * 0.7)
print(f'I need {total_pizza} pizzas to feed {friends} friends')

my_date = datetime.date(2020, 12, 2)
print(my_date)
print(my_date.strftime("%d-%b-%Y"))
# second print statement changes the date formatting

#for loops
for number in range(10):
    print(f'Number:{number + 1}')

for name in ['Taryn', 'Chris', 'Lola']:
    print(name)

#while loops
store_capacity = 2

while store_capacity > 0:
    print('Please come in. Spaces avaliable: '+str(store_capacity))
    store_capacity = store_capacity - 1

print("\nPLease wait for someone to leave!")

#functions
def hello(name):
    print(f'Hello, Good Evening {name}!')
hello('Taryn')
hello('Chris')
hello('Lola')

def my_job(name, job):
    print(name, 'is a', job)

my_job('taryn', 'developer')
my_job(job='shitten', name='Lola')
# #two different ways

def my_city(name, city="perth"):
    print(name, city)
my_city('Taryn')


def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

circle_1 = circle_area(10)
print(circle_1)

#
def days_in_hours(days):
    hours = days * 24
    return hours
print(days_in_hours(10))

#combining for loop and function
def times_two(num):
    result = num * 2
    return result

for number in range(2):
    calc_res = times_two(number)
    print(calc_res)

