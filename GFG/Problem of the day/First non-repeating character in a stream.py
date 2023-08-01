#User function Template for python3
import time
class Solution:
	def FirstNonRepeating(self, A):
	    charcount = {}
	    nonRepeatchar = []
	    result = ""
	    for c in A:
	        if c not in charcount:
	            charcount[c] = 1
	        else:
	            charcount[c] += 1
	        nonRepeatchar.append(c)
	        while nonRepeatchar and charcount[nonRepeatchar[0]] > 1:
	            nonRepeatchar.pop(0)
	        if not nonRepeatchar:
	            result += '#'
	        else:
	            result += nonRepeatchar[0]
	    return result


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends