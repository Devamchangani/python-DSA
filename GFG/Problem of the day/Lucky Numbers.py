#User function Template for python3

class Solution:
    def check(self, n, i):
        return (n % i != 0) and ((n < i) or self.check(n - n // i, i + 1))
    
    def isLucky(self, n):
        return self.check(n, 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends