num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print( num1, "NUmber  is greater then ")
elif(num2>num3 and num2>num4):
    print(num2, "Number  is greater then")
elif(num3>num4):
    print(num3, "Number is greater then")        
else:
    print(num4, "Number 4 is greater then")    