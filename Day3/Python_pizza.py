#

print("Welcome to the Python Pizza Deliveries!")
size = input("what size of pizza do you want ? S , M , L: ")
peproni = input("Do you want pepperoni ? Y or N : ")
extra_cheese = input("Do you want extra cheese ? Y or N : ")
bill = 0 

if size == "l":
    bill += 25

elif size == "m":
    bill += 20

elif size == "s":
    bill += 15
    if peproni == "y":
        bill += 1


if peproni == "y" and (size == "m" or size == "l"):
    bill +=3     

if extra_cheese == "y":
    bill = bill + 1

print(f"your total bill is {bill}$")    