# a = int(input("Enter a decimal number: "))
# #this will print a in binary
# bnr = bin(a).replace('0b','')
# x = bnr[::-1] #this reverses an array
# while len(x) < 8:
#     x += '0'
# bnr = x[::-1]
# print(bnr)

lst = []
def find(b):
    bnr = bin(b).replace('0b','')
    x = bnr[::-1] #this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)


n = int(input("number of decimal"))
for i in range(0,n): 
    b = int(input("enter a number: "))
    lst.append(b)
    
for b in lst: 
    print(find(b))