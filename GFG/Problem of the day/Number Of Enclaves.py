#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
    
        def dfs(row, col):
            stack = [(row, col)]
            count = 0
    
            while stack:
                r, c = stack.pop()
                if (
                    r < 0
                    or r >= len(grid)
                    or c < 0
                    or c >= len(grid[0])
                    or grid[r][c] == 0
                ):
                    continue
    
                grid[r][c] = 0  # Mark the cell as visited
                count += 1
    
                # Add adjacent cells to the stack
                stack.append((r - 1, c))
                stack.append((r + 1, c))
                stack.append((r, c - 1))
                stack.append((r, c + 1))
    
            return count
    
        # Start DFS from the boundary land cells
        for row in range(len(grid)):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][len(grid[0]) - 1] == 1:
                dfs(row, len(grid[0]) - 1)
    
        for col in range(len(grid[0])):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[len(grid) - 1][col] == 1:
                dfs(len(grid) - 1, col)
    
        # Count the remaining land cells (those not connected to the boundary)
        enclave_count = sum(row.count(1) for row in grid)
    
        return enclave_count
    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends