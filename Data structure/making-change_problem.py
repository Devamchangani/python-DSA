
def value():
    r = int(input("Enter the amount for which you want change:"))
    n = int(input("Enter total number of coins:"))
    print("Enter the values for coin:")
    co = []
    for i in range(n):
        co.append(int(input()))
    return r,n,co

# Making Change Problem using dynamic programming
def count(co, n, r):
    c = [[0 for i in range(r+1)]for i in range(n)]
    
    for i in range(r+1):
        c[0][i] = i
    for i in range(1, n):
        for j in range(1, r+1):
            c[i][j] = min(c[i-1][j], (c[i][j-(co[i])]+1))
    
    print("Count Table:\n") 
    for i in range(n):
        print(*c[i], sep=" | ")
    
    ans = []
    i = n-1
    j = r
    while (i != 0):
        if c[i][j] == c[i-1][j]:
            i = i-1
            if i == 0:
                ans.append(co[i])
        else:
            j = j-co[i]
            ans.append(co[i])
    
    ans.reverse()
    print("\n")
    print("The changes for given coin values will be:", ans)


if __name__ == "__main__":

    r,n,co = value()
    count(co, n, r)
