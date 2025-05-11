print("Welcome to Pizza Deliveries!")
size = input("What size would you like? S, M or L")
bill = 0

if size == "S":
    bill = 15
    pepperoni = input("Add extra Pepperoni? Y or N")
    cheese = input("Extra Cheese, Y or N?")
    if pepperoni == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    pepperoni = input("Add extra Pepperoni? Y or N")
    cheese = input("Extra Cheese, Y or N?")
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
else:
    bill = 25
    pepperoni = input("Add extra Pepperoni? Y or N")
    cheese = input("Extra Cheese, Y or N?")
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
print(f"your final bill is ${bill}")
