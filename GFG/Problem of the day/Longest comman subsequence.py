#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        matrix=[[0 for s1 in range(y+1)] for s1 in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        print("table")
        print(matrix)     
        return matrix[x][y]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends