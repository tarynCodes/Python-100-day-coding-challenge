#If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
#
# Format the result to 2 decimal places = 33.60
#
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

print("welcome to the tip calculator")
bill =float(input("How much is your bill? £"))
tip = int(input("What tip would you like to give? 10, 12 or 15? "))
people = int(input("How many ways would you like to split the bill? "))

tip_amount = tip / 100
total_tip_amount = bill * tip_amount
total_per_person = (bill + total_tip_amount) / people
final_amount = "{:.2f}".format(total_per_person)

print(f"Each person should pay: £{final_amount}")
