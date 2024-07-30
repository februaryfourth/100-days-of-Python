print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") 
name2 = input("What is their name?")  
# Your code below this line 👇

add_names = name1 + name2
lower_case = add_names.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t+r+u+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l+o+v+e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")