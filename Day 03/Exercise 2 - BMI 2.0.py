# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    interpretation = "underweight"
elif bmi < 25:
    interpretation = "normal weight"
elif bmi < 30:
    interpretation = "slightly overweight"
elif bmi < 35:
    interpretation = "obese"
else:
    interpretation = "clinically obese"

print(f"Your BMI is {bmi}, you are {interpretation}.")