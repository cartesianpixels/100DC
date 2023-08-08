# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_factor = float(height)
weight_factor = float(weight)
bmi = weight_factor / (height_factor ** 2)
f_bmi = int(bmi)
print("your BMI is :" , f_bmi)