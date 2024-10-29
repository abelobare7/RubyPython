# create a program that checks a student performance
marks=int(input("Enter Marks "))

# if marks<=100 and marks>=80
if 100>= marks >=80:
    print("You have an A")
elif 79>= marks >=60:
    print("You have a B")
elif marks<=59 and marks>=49:
    print("You have a C")
elif marks<=39 and marks>=0:
    print("You have failed")
else:
    print("Invalid Marks")

# bmi calculator
weight=int(input("Enter your weight: "))
height=float(input("Enter your height: "))
BMI=weight/(height**2)

if BMI<18.5:
    category = "Underweight"
elif BMI>=18.5 and BMI<25:
    category= "Normal"
elif BMI>=25 and BMI<30:
    category= "Overweight"
else:
    category= "Obeise"

print(f"\nYour Bmi is: {round(BMI, 2)}")
print(f"Category: {category}")