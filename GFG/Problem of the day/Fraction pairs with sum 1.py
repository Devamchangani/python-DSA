#User function Template for python3
import math
class Solution:
    def countFractions(self, n, numerator, denominator):
        # Your code here
        m = {}
        ans = 0
        for i in range(n):
            gcd = math.gcd(numerator[i], denominator[i])
            numerator[i] //= gcd
            denominator[i] //= gcd
            x = numerator[i]
            y = denominator[i]
            z = y - x
            if (z, y) in m:
                ans += m[(z, y)]
            m[(numerator[i], denominator[i])] = m.get((numerator[i], denominator[i]), 0) + 1
        return ans

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends