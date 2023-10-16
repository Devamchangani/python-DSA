from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx == pary:
            return
        if self.size[parx] > self.size[pary]:
            self.parent[pary] = parx
            self.size[parx] += self.size[pary]
        else:
            self.parent[parx] = pary
            self.size[pary] += self.size[parx]


class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        n = len(grid)
        ds = DSU(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    now = i * n + j
                    if j + 1 < n and grid[i][j + 1]:
                        ds.union(now, i * n + j + 1)
                    if j >= 1 and grid[i][j - 1]:
                        ds.union(now, i * n + j - 1)
                    if i + 1 < n and grid[i + 1][j]:
                        ds.union(now, (i + 1) * n + j)
                    if i >= 1 and grid[i - 1][j]:
                        ds.union(now, (i - 1) * n + j)
        if ds.size[ds.find(0)] == n * n:
            return n * n
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    res = 1
                    pars = set()
                    if i+1 < n and grid[i+1][j]:
                        pars.add(ds.find((i+1)*n+j))
                    if i-1 >= 0 and grid[i-1][j]:
                        pars.add(ds.find((i-1)*n+j))
                    if j+1 < n and grid[i][j+1]:
                        pars.add(ds.find(i*n+j+1))
                    if j-1 >= 0 and grid[i][j-1]:
                        pars.add(ds.find(i*n+j-1))
                    for itr in pars:
                        res += ds.size[itr]
                    ans = max(ans, res)
        return ans
                    
#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends