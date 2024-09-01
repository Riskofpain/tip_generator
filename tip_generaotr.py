print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage = 1 + tip / 100

split = bill * percentage / people

split_round = round(split, 2)

print(f"Each person should pay: ${split_round}")
