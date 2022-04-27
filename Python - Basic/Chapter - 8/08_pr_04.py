#  sum(n) = sum(n-1)+n


def Sum_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n + Sum_recursive(n-1)


def sum_iter(n):
    product = 0
    for i in range(n):
        product = product + (i+1)
    print(product) 

 
sum_iter(15)
S = Sum_recursive(15)
print(S)