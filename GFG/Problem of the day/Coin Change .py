#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # code here 
        prev = [0] * (sum + 1)
        for i in range(sum + 1):
            if i % coins[0] == 0:
                prev[i] = 1
        for i in range(1, N):
            curr = [0] * (sum + 1)
            for j in range(sum + 1):
                a, b = 0, 0
                a = prev[j]
                if j >= coins[i]:
                    b = curr[j - coins[i]]
                curr[j] = a + b
            prev = curr
        return prev[sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends