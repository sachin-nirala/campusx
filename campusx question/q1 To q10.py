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