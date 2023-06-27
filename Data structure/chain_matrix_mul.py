def value():
    n=int(input("Enter the total number of matrices:"))
    data=[]
    for i in range(n):
        r=int(input("Enter the number of rows in matrix {}:".format(i+1)))
        data.append(r)
    x=int (input("Enter the number of columns in matrix : "))
    data.append(x)
    
    return data,n

#Chain Matrix
def product(p):
    n = len(p)
    m = [[-1]*(n) for _ in range(n)]
    s = [[-1]*(n) for _ in range(n)]
    product_h(p,1,n-1,m,s)
    
    print("M:")
    
    for i in range(n):
        for j in m:
            print(j[i],end='\t')
        print()
    
    print("S:")
    
    for i in range(n):
        for j in s:
            print(j[i],end='\t')
        print()
    return m,s


def product_h(d,st,e,m,s):
    if m[st][e]>=0 :
        return m[st][e]
    if st==e:
        a=0
    else:
        a=float('inf')

    for i in range(st,e):
        h= product_h(d,st,i,m,s) + product_h(d,i+1,e,m,s)+d[st-1]*d[i]*d[e]
        if h<a:
            a=h
            s[st][e]=i
    m[st][e]=a
    return a

#Parentheses
def parentheses(s,st,e):
    if st==e:
        print('A[{}]'.format(st), end ='')
        return

    k=s[st][e]
    print('(', end='')
    parentheses(s,st,k)
    parentheses(s,k+1,e)
    print(')', end='')


if __name__ == "__main__":
    data,n = value()

    m,s=product(data)
    print("The number of scalar multiplication required :",m[1][n])
    print("Optimal parenthesization for multiplication:",end='')
    parentheses(s,1,n)
