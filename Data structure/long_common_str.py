def value():
    X=[x for(x) in input("Enter String X separates by space:").split()]
    Y=[x for(x) in input("Enter String Y separated by space:").split()]
    return X,Y
#Longest Common Subsequence using dynamic programming
def lcs(x,y,m,n):
    matrix=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                matrix[i][j]=0
            elif x[i-1]==y[j-1]:
                matrix[i][j]=matrix[i-1][j-1]+1
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    print("TABLE:")
    print(matrix)
    index=matrix[m][n]
    lcs=[""]*(index+1)
    lcs[index]=""
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs[index-1]=x[i-1]
            i -=1
            j-=1
            index -=1
        elif matrix[i-1][j]>matrix[i][j-1]:
            i-=1
        else:
            j-=1

    return lcs


if  __name__ == "__main__":
    X,Y = value() 

    m=len(X)
    n=len(Y)
    ans="".join(lcs(X,Y,m,n))
    print("Here, Longest common subsequence is:",ans)