print("Welcome to the roller coaster!")
hight = int(input("what is your hight in cm ?"))
age = int(input("what is your age ?"))

if hight >= 120:
   if age > 18:
        print("you can go and need to pay 18 $")
   elif 12 <= age <= 18:
        print("you can go and need to pay 7 $")
   else:
        print("you can go and pay 5 $")         

else:
    print("you cant sorry try next year")    
