# User function Template for python3

class Solution:
	def Count(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    continue
                else:
                    if self.bfs(i, j, matrix):
                        count += 1
        return count


    def __init__(self):
        self.dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        self.dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    def bfs(self, row, col, matrix):
        n = len(matrix)
        m = len(matrix[0])
        count0 = 0
        for i in range(8):
            delRow = row + self.dx[i]
            delCol = col + self.dy[i]
            if delRow >= 0 and delCol >= 0 and delRow < n and delCol < m and matrix[delRow][delCol] == 0:
                count0 += 1
        if count0 % 2 == 0 and count0 > 0:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends