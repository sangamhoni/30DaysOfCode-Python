# WAP to calculate the Body Mass Index

height = float(input("enter your height in m:  "))
weight = float(input("enter your weight in kg: "))

BMI=round(weight/(height**2))

print(BMI)

