# Question :( 1.)--------------------------------------------------------------------------------------------------------------------------------------------------
n1 = int(input("Enter 1st number:-  "))
n2 = int(input("Enter 2nd number:-  "))
n3 = int(input("Enter 3rd number:-  "))
if n1 > n2 and n1 > n3:
    print(n1, " is greastest")
elif n2 > n1 and n2 > n3:
    print(n2, " is greatest.")
elif n3 > n1 and n3 > n2:
    print(n3, "is greatest.")


# Question:--(2)-------------------------------------------------------------------------------------------------------------------
n1 = int(input("Enter 1st number:-  "))
temp = n1
n2 = int(input("Enter 2nd number:-  "))
print( "first", n1, "second", n2)
n1 = n2
n2 = temp

print("updated numbers n1 and n2 are", n1,n2)

# Question:- (3.)--------------------------------------------
#Write a program that will give you the sum of 3 digits
celsius = int(input("Enter celcious temprature:--"))
fahrenheit = celsius * 1.8 + 32
print(f"C = {celsius} and f = {fahrenheit}" )


#Question:- (4.)--------------------------------------------
#Write a program that will give you the sum of 3 digits
n1 = int(input("Enter first number:"))
n2 = int(input("Enter 2nd number:"))
n3 = int(input("Enter 3rd number:"))
sum = n1 + n2 + n3
print(f"Total is {sum}")

# Question:- (5.)--------------------------------------------
# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
num = input("Enter four digits number:-")
r_num = num[::-1]

print(f"first number {num} and 2nd reverse number:= {r_num}")
if r_num == num[::-1]:
    print("True")
else:
    print("False")



# Question:- (6.)--------------------------------------------
# Write a program that will tell whether the number entered by the user is odd or even.

num = int(input("Enter a digits number:-"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question:- (7.)--------------------------------------------
#Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter a Year:-"))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
         print("leap year")
else:
    print("Not leap year")



# Question:- (10)--------------------------------------------
# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
c_price = float(input("chal product ka cost price bta."))
s_price = float(input(" And selling price bhi bata."))
revenue_cost = s_price - c_price
if revenue_cost < 0:
    print(f"you lost {revenue_cost}rs")
else:
    print(f"you are in profit and your profit is {revenue_cost}rs")