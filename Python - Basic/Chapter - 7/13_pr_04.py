num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if (num%i ==0):
        prime = False
        break
if prime:    
    print("this number is prime")
else:
    print("This is a not prime")    