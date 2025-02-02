weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi >= 25:
    print("overweight")
elif bmi < 18.25:
    print("underweight")
elif 25 > bmi >= 18.5:    
    print("normal weight")

    