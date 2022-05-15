from operator import index


list = [5, False, 52, "Devam", 5.8]

# index = 0
# for item in list:
#     print(item, index)
#     index += 1 


for index, item in enumerate(list):
    print(item, index) 