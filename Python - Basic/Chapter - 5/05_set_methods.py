# creating an empty set

b = set()
print(type(b))

# adding a value in set
b.add(8)
b.add(17)


b.add((5, 8, 9)) #can add tuple to set
#b.add({4:5}) #cannot add list or dictionory to set

print(b)