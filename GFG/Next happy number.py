#User function Template for python3


class Solution:
    def nextHappy (self, N):
        # code here
        x = 0
        input = N+1
        while(x==0):
            # self.solve(input)
            if self.solve(input) == True:
                return input
            else:
                input += 1
        return -1
    
    def solve(self, input):
        if (input == 1 or input == 7):
            return True
        if input < 10:
            return False
            
        temp = 0
        while(input != 0):
            x = input%10
            input = input // 10
            temp += x * x
        
        input = temp
        return self.solve(input)
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends