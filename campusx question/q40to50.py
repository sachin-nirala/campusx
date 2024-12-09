print("This is 50")
# question (58.) ---Write a python program to remove all the duplicates from a list.
l = [1,2,34,3,3,33,3,1,1,11,1,1," ","",'sachin','nirala','sachin','raju']
u_list = []
for i in l:
    
    if i not in u_list:
        u_list.append(i)

print("This unic list:= ",u_list)


# Question(59)Write a python program to convert a string to title case without using the title()
s = "sachin is a good, smart and hardworking man."
s_title = s.split(" ")
n = []
print(s_title)
for i in s_title:
    n.append(i.capitalize() + " ")
    s_title = ''.join(n)
print(s_title)
 #(61.)Write a python program to reverse a list
l = ['Sachin', 1,3,4, [1,23,'sachin'], 2,4]
print(l[::-1])
print(l)
r_list = []
for i in l:
    r_list = l.reverse()
print(r_list)

