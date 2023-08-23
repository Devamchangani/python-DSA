#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        rows = len(grid)
        cols = len(grid[0])
        result = []
        visited = set()
    
        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < cols
    
        def checkDirection(x, y, dx, dy):
            for char in word:
                if not isValid(x, y) or grid[x][y] != char:
                    return False
                x += dx
                y += dy
            return True
    
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    if checkDirection(i, j, dx, dy) and (i, j) not in visited:
                        visited.add((i, j))
                        result.append((i, j))
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends