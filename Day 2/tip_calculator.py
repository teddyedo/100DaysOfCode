print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? "))
percentageTip = float(input("What percentage tip would you lke to give? "))
eaters = int(input("How many were you?"))

totalCostOfMeal = totalBill * round(percentageTip / 100 + 1, 2)

# Forcing price per person to a 2 float digits number
priceForPerson = "{:.2f}".format(round(totalCostOfMeal / eaters, 2))

print(f"Each person should pay {priceForPerson} €")
