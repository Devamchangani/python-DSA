#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
        dp = [[-1] * (sum + 1) for _ in range(n + 1)]
        return self.solve(0, arr, n, sum, dp)


    def solve(self, ind, arr, n, sum_left, dp):
        if sum_left < 0:
            return 0
        if ind == n and sum_left == 0:
            return 1
        if ind >= n:
            return 0
        if dp[ind][sum_left] != -1:
            return dp[ind][sum_left]
        MOD = 10**9 + 7
        ans = (self.solve(ind + 1, arr, n, sum_left - arr[ind], dp) % MOD) + (self.solve(ind + 1, arr, n, sum_left, dp) % MOD)
        ans %= MOD
        dp[ind][sum_left] = ans
        return dp[ind][sum_left]
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends