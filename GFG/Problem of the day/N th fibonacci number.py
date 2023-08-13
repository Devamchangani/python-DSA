
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        f = 1
        s = 1
        m = 1000000007
        l = 0
        for i in range(n-2):
            l = f+s
            f = s
            s = l
        print(l)
        print("")
        print(l%m)
        # return s
        
        # m = 10**9 + 7
        # a, b = 0, 1
        # for i in range(2, n+1):
        #     c = (a + b) % m
        #     a, b = b, c
        # return b


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends