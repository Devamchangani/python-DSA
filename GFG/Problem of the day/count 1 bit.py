# User function Template for python3
class Solution:
    def setBits(self, N):
        count = 0
        while N:
            last_bit = (N & 1)
            count += last_bit
            N = N >> 1
        return count
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends