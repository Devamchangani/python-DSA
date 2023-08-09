#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        i = 2
        while i*i <= N:
            n = i*i
            while(N % i == 0):
                N //= i
            i += 1
        if (N > 1):
            return N
        return i-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends