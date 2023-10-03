#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        ans = ""
        while(n):
            n -= 1
            ch = chr(ord('A') + n % 26)
            ans += ch
            n //= 26
        return ans[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends