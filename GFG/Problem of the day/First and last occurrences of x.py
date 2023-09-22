#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        l = []
        for i in range(n):
            if arr[i] == x:
                l.append(i)
                for j in range(i,n):
                    if arr[j] == x:
                        s = j
                    else:
                        l.append(j-1)
                        break
                if j == n-1:
                    l.append(s)
                break
            if i == n-1:
                l = [-1,-1]
        return l
#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends