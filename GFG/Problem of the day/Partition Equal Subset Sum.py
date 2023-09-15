# User function Template for Python3

class Solution:
    def equalPartition(self, n, arr):
        # code here
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        return self.targetSum(arr, n, total_sum // 2)


    def targetSum(self, arr, n, target):
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(n):
            for t in range(target, arr[i] - 1, -1):
                dp[t] |= dp[t - arr[i]]
        return dp[-1]
        
#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
#     } Driver Code Ends 