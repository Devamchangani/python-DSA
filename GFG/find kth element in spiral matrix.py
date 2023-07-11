#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        ans = []
        l = 0
        r = m - 1
        t = 0
        d = n - 1
        while l <= r and t <= d:
            for j in range(l, r + 1):
                ans.append(a[t][j])
            t += 1
            for i in range(t, d + 1):
                ans.append(a[i][r])
            r -= 1
            for j in range(r, l - 1, -1):
                ans.append(a[d][j])
            d -= 1
            for i in range(d, t - 1, -1):
                ans.append(a[i][l])
            l += 1
        return ans[k - 1]


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends