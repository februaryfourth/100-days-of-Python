year = int(input("Input a year you want to check is a leap year: "))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is a not leap year.")
    