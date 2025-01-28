print("Welcome to the tip calculator!")

total_bill = float(input("What was the totlal bill? $\n"))
tip_precentage = int(input("How much tip whould you like to give ? 10, 12, or 15 ?\n"))/100
number_of_pepole = int(input("How many pepole are going to share the bill?\n"))
Perconal_bill = ((1+tip_precentage)* total_bill)/number_of_pepole
round_personal_bill = round(Perconal_bill, 2)

# print(Perconal_bill)

print(f"Each Person should pay {round_personal_bill}")
 