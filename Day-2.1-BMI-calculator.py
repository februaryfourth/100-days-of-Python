
# bmi = Weight/Height(2)

height = float(input("What is your height"))
weight = int(input("What is your weight?"))

bmi=int(weight / (height*height))
print(bmi)
print("Your bmi would be " + str(bmi))