# PYTHON 

def minvalyu(a, b, n):
    
    a.sort()
    b.sort()
    b.reverse()
    
    sum = 0
    
    for i in range(n):
        sum += a[i] * b[i]
    return sum

if __name__ == "__main__":
    n = int(input("Enter a number of element: "))
   
    a = []
    b = []
    for i in range(n):
        c = int(input("Enter a first element: "))
        a.append(c)
    
    print("   ")
    
    for i in range(n):
        c = int(input("Enter a second element: "))
        b.append(c)
    
    s = minvalyu(a, b, n)
    print(s)