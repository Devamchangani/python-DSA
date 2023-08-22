#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        col = [0] * n
        row = [0] * n
        maxsum = 0
        for i in range(n):
            for j in range(n):
                col[j] = col[j] + matrix[i][j]
                row[i] = row[i] + matrix[i][j]
                maxsum = max(maxsum, col[j])
                maxsum = max(maxsum, row[i])
        count = 0
        for i in range(n):
            for j in range(n):
                maxi = max(col[j], row[i])
                inc = maxsum - maxi
                if inc == 0:
                    continue
                else:
                    col[j] = col[j] + inc
                    row[i] = row[i] + inc
                    count = count + inc
        return count


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends