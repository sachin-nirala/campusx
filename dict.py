#how to create a dictionary
# dictionary is mutable types
# keys should be unique
# it is key values pair
#dictoionay has no indexing.

d = {}
d = {'Name':'Sachin', 'class':3,'marks':{'hindi':'hundred', 'English':89, "English": 99}}
print(d)
# how to access items in dictionary
print(d["marks"])
 #How to EDIT in dictionary
d['Name'] = 'Rahul'
print(d)
# How to update dict... throught get() methord
print(d.get('marks').get('hindi'))
# ----------------------OR----------------
print(d['marks']['hindi'][3])
#-----------------------------------OR--------------------------------- 
print(d.get('marks').get('hindi')[2])

