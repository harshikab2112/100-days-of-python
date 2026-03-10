print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = bill + (bill * tip / 100)
# total = bill * (1 + tip / 100)

each_person_share = total / people

print(f"Each person will pay: ${each_person_share:.2f}")
