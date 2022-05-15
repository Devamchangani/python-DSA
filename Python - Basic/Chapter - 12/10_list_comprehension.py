
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# b = []

# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

# Shortcut to write the same
b = [i for i in a if i%2==0]
print(b)


j = [1, 4, 5, 4, 1, 8, 5, 9]
k = {i for i in j}
print(k)