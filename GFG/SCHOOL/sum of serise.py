# User function Template for python3

class Solution:

    def seriesSum(self, n):
#   with for loop
        sum = 0
        # for i in range(1,n+1):
        #     print(i)
        #     sum += i

        # return sum


# With while loop
        while(n != 0):
            sum += n
            n -= 1
        return sum


#   with recursion
        # if n == 0:
        #     return 0
        # return n + self.seriesSum(n - 1)


        s = (n*(n+1))//2
        return s

# {
 # Driver Code Starts
    # Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc = tc-1
# } Driver Code Ends
