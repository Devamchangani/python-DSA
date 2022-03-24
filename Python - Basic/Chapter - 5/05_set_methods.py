# creating an empty set

from os import remove

b = set()
print(type(b))

# adding a value in set
b.add(8)
b.add(17)
b.add(17)# adding a value repeatedly does not changes a set

b.add((5, 8, 9)) #can add tuple to set
print(b)
b.add((54,83,999))
print(b)

#b.add({4:5}) #cannot add list or dictionory to set


# print a lrnghth of set
print(len(b))

# remove the value
b.remove(17)
print(b)



