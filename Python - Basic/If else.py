# age = 14
# if age < 18:
#    print("you are a children")
# else:
#    print("you are a young")

a = int(input("Enter Number of value : "))
c = 0
for i in range(1, a+1):
   b = int(input(f"Enter {i} value : "))
   c = c+b

ans = c/a
print(ans)

