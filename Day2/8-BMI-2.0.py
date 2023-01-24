# WAP to find the Body Mass Index and check which criteria they fall in

height = float(input("enter your height in m:  "))
weight = float(input("enter your weight in kg: "))

BMI=round(weight/(height**2))
print(f"Your BMI is {BMI}")

if(BMI<18.5):
    print("You're underweight")
elif BMI<25:
    print("You have a normal weight")
elif BMI <30:
    print("You're overweight")
elif BMI<35:
    print("You're obese")
else:
    print("You're clinically obese")

