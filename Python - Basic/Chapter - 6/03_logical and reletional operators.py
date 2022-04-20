
# logical operator = ("==, >=, <=, etc")
# relational operator = (and, or, not)

age = int(input("Enter your age: "))

if (age>=18 and age<50):
    print("you can work")
elif (age>6 and age<18):
    print("you are children")
else:
    print("you are older")        