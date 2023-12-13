# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

take_umbrella = input('is it raining outside? (y/n)')
is_raining = take_umbrella == 'y'
is_not_raining = take_umbrella == 'n'
if is_raining:
    print('Take an umbrella')
elif is_not_raining:
    print('you dont need an umbrella')

# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong
my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if float(my_money) > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century, Seventies")


book_year = int(input('What year was your book written?'))

eighteenth_century = 1700 <= book_year <= 1800
nineteenth_century = 1801 <= book_year <= 1900
twentieth_century = 1901 <= book_year <= 2000

if eighteenth_century:
    print('Eighteenth Century')
    decade = (book_year - 1700) // 10
    print(f'Decade: {decade}th')
elif nineteenth_century:
    print('Nineteenth Century')
    decade = (book_year - 1800) // 10
    print(f'Decade: {decade}th')
elif twentieth_century:
    print('Twentieth Century')
    decade = (book_year - 1900) // 10
    print(f'Decade: {decade}th')
else:
    print('Not in the specified centuries')

