import numbers
import string


# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     print(squared_numbers)

# numbers = [2,5,6,9]
# get_squared_numbers(numbers)

numbers = [3,6,3,5,2,4,5]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i] )
            print("is a duplicate")
            break