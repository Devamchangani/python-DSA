# # Initialize list
# Lst = [-2,]
 
# # Display list
# print(Lst[::])
# print(Lst[1::])
# print(Lst[1:5:])
# print(Lst[1:5:2])
# print(Lst[::-1])

# Initializing list
test_list = [1, 2, 3, 1, 3, 4]
ls = []
ls1 = []
# Checking if 4 exists in list
for i in test_list:
    if(i == 1 or i == 2):
        ls.append(i+3)
print(ls)      


ls1.append(test_list[4]-7)

print(ls1)

Sum = sum(test_list[3:7:])
print(Sum)