#Type error
# use type() to check the type of data
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill: £"))
tip_percent = int(input("How much tip would you like to give? 10, 12, 0r 15?"))
num_people=int(input("How many people to split the bill?"))
bill_per_person = total_bill / num_people
tip_per_person = total_bill * (tip_percent/100)
total_per_person =round(bill_per_person + tip_per_person)
final_amount ="{:.2f}".format(total_per_person)
print(f"Each person should pay: £{final_amount}")