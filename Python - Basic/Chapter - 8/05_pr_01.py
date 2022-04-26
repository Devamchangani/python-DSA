def maximum(num1, num2, num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is maximum")
    elif num2>num3:
        print(f"{num2} is maximum")
    else:
        print(f"{num3} is maximum")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

maximum(num1, num2, num3)