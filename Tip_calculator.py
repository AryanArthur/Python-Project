#Tip Calculator
print("Welcome to the tip calculator")
Total_Bill = float(input("What is the total bill? $ "))
Tip = int(input("How much tip would you like to give?, 10, 12 or 15?"))
Bill_Split = int(input("How many people to split the bill?"))

x = Tip/100
Total_Amount = Total_Bill*x + Total_Bill
Individual_Amount = Total_Amount/Bill_Split
Overall = round(Individual_Amount, 2)
print(f"Each person should pay: ${Overall}")
