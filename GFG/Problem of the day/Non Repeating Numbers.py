#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		dict = {}
		l = []
		l2 = []
		for i in nums:
			if i not in dict:
				dict[i] = 1
			else:
				dict[i] += 1
# 		print(dict)
        
		for i in dict:
			if dict[i] == 1:
				l.append(i)

		l.sort()
		return l
		

# WITH THIS SOLUTION MORE TIME 
# 		for i in nums:
# 			if i in l2:
# 				continue
# 			else:
# 				if i not in l:
# 					l.append(i)
# 				else:
# 					l.remove(i)
# 					l2.append(i)
		# l.sort()
		# return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends