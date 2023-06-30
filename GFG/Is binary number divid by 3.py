#User function Template for python3
class Solution:
	def isDivisible(self, s):
		# code here
		# return int(s,2)
		# a = s
		a = self.solve(s)
		# print(a)

		if a % 3 == 0:
			return 1
		else:
			return 0

		

	def solve(self,s):
		return int(s,2)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends