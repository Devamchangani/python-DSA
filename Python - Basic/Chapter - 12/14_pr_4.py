a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))

try:
    print(a/b)
except ZeroDivisionError:
    print("infinite")
