# this is day 2 of 100 days of code in python

print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

number_of_people = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
percentage_float = float(percentage)/100
number_of_people_float = float(number_of_people)

result = (total_bill_float + (total_bill_float * percentage_float))/number_of_people_float

print("Each person should pay: $" + str(round(result, 2)))
