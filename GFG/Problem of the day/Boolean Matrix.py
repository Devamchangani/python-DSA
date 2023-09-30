#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(v):
    # code here 
    n = len(v)
    c = len(v[0])
    
    # Initialize arrays to track rows and columns to be updated
    row_flag = [0] * n
    col_flag = [0] * c
    
    # Identify rows and columns with 1s and update the flags
    for i in range(n):
        for j in range(c):
            if v[i][j] == 1:
                row_flag[i] = 1
                col_flag[j] = 1
    
    # Update the matrix based on the flags
    for i in range(n):
        for j in range(c):
            if row_flag[i] == 1 or col_flag[j] == 1:
                v[i][j] = 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends