#User function Template for python3

class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        
    def fill(self, n, m, mat):
        # code here
        for i in range(n):
            for j in range(m):
                if self.isBoundary(i, j, n, m) and mat[i][j] == 'O':
                    self.setNotClosed(i, j, n, m, mat)
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'N':
                    mat[i][j] = 'O'
        
        return mat
    
    
    def isValid(self, ii, jj, n, m):
        return ii >= 0 and jj >= 0 and ii < n and jj < m
    
    def isBoundary(self, i, j, n, m):
        return i == 0 or j == 0 or i == n - 1 or j == m - 1
    
    def setNotClosed(self, i, j, n, m, mat):
        mat[i][j] = 'N'
        for d in range(4):
            ii = self.dx[d] + i
            jj = self.dy[d] + j
            if self.isValid(ii, jj, n, m) and mat[ii][jj] == 'O':
                self.setNotClosed(ii, jj, n, m, mat)
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends