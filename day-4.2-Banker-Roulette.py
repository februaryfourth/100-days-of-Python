import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

number = len(names)
choice = random.randint(0,number-1)
selected = names[choice]
print(f"{selected} is going to buy the meal today!")