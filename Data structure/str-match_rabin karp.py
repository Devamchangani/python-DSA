def value():
    s=input("Enter the string:")
    p=input("Enter the pattern:")
    q=int(input("Enter the prime number:"))
    return s,p,q

#String Matching using Robin-Karp algorithm
d=256

def pattern(p,s,q) :
    m=len(p)
    n=len(s)
    i=0
    j=0
    pa=0
    t=0
    o=1
    for i in range(d,m-1):
        o=(o*d)%q
    
    for i in range(m):
        pa=(d*pa + ord(p[i]))%q
        t=(d*t + ord(s[i]))%q

    for i in range(n-m+1):
        if pa==t:
            for j in range(m):
                if s[i+j]!=p[j]:
                    break
            j += 1
            if j==m:
                print("Pattern of string found at index:"+str(i+1))
    if i < n-m :
        t=(d*(t-ord(s[i]*o)+ord(s[i+m]))%q)

    if t<0 :
        t=t+q


if __name__ == "__main__":
    s,p,q = value()
    pattern(p,s,q)