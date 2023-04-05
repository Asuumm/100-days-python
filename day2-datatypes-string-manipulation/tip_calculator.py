# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number.
# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_calc = int(tip) / 100
people = input("How many people to split the bill? ")
amount_total = (float(bill) / float(people)) * float(tip_calc + 1)
amount = round(amount_total, 2)
# to get the 2 decimals to display 00 you need to format for it to show = "{:.2f}".format(variable_name)
# learnt this after doing the assignment.
print("Each person should pay: $" + str(amount))

