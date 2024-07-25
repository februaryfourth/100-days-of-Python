height = float(input("What is your height in Meters i.e 1.55: "))
weight = int(input("What is your weight in KG i.e 72: "))

#calculate bmi
bmi = weight / (height*2)

# Create the conditions

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
     print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
     print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
     print(f"Your BMI is {bmi}, you are obese.")
else:
       print(f"Your BMI is {bmi}, you are clinically obese.")
