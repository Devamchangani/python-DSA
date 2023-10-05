#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        # your code here
        return self.f(s, k) - self.f(s, k - 1)

    def f(self, s, k):
        if k < 0:
            return 0
        lo = 0
        hi = 0
        ans = 0
        n = len(s)
        cnt = 0
        A = [0] * 26
        while hi < n:
            A[ord(s[hi]) - ord('a')] += 1
            if A[ord(s[hi]) - ord('a')] == 1:
                cnt += 1
            while cnt > k:
                A[ord(s[lo]) - ord('a')] -= 1
                if A[ord(s[lo]) - ord('a')] == 0:
                    cnt -= 1
                lo += 1
            ans += (hi - lo + 1)
            hi += 1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends