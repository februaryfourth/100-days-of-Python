### If statements
print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaset")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You pay £5")
    elif age <= 18:
        bill = 7
        print("You pay £7")
    else:
        bill = 12
        print("You pay £12")
    want_photos = input("Would you want photos for £3 extra? Enter Y or N: ")
    if want_photos == "y":
        bill += 3
    print(f" Your total bill is {bill}")
else: 
    print("Sorry, you have to grow taller before you can ride")


#Odd or even number

number = int(input("Select a number for me to guess if it's odd or even: "))

if number % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number")


#Nested if statement using if else

