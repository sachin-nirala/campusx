
# how to filter a list.
#suppose s = ['sachin', 1,2,3,3,1,1,2,2,'sachin','suraj']

s = ['sachin', 1,2,3,3,1,1,2,2,'sachin','suraj']
filter_s = []

for i in s:
    if i not in filter_s:
        filter_s.append(i)
print(filter_s)