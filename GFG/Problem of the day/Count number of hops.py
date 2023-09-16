#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,N):
        
        # code here
        if N <= 1:
            return 1
    
        MOD = 1000000007
        dp = [0] * (N + 1)
        dp[0] = 1
    
        for i in range(1, N + 1):
            for j in range(1, 4):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
    
        return dp[N]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends