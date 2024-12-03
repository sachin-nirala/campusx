# Question:- (10)--------------------------------------------
# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
c_price = float(input("chal product ka cost price bta."))
s_price = float(input(" And selling price bhi bata."))
revenue_cost = s_price - c_price
if revenue_cost < 0:
    print(f"you lost {revenue_cost}rs")
else:
    print(f"you are in profit and your profit is {revenue_cost}rs")
    print("This is Sachin this side.")