def value():
    n=int(input("Enter total number of rows in chessboard:"))
    m=[['-' for x in range(n)] for y in range(n)]
    return n,m


# N Queen Problem
def safe(m,r,c):
    for i in range(r):
        if m[i][c] == 'Q' :
            return False

    (i,j)=(r,c)
    
    while(i>=0 and j>=0):
        if m[i][j] == 'Q' :
            return False
    
        i-=1
        j-=1
    (i,j)=(r,c)

    while(i>=0 and j<len(m)):
        if m[i][j] == 'Q' :
            return False
        i-=1
        j+=1
    
    return True


def sol(m):
    print("    ")
    print("    ")
    for i in m:
        print(str(i).replace(',','|'))
        print()

def nq(m,r):
    if r==len(m):
        sol(m)
        return

    for i in range(len(m)):
        if safe(m,r,i):
            m[r][i] = 'Q'
            nq(m,r+1)
            m[r][i] = '-'


if __name__ == "__main__":
    n,m = value()
    nq(m,0)