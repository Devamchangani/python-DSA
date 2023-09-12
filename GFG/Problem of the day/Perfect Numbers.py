#User function Template for python3
import math
class Solution:
    def isPerfectNumber(self, N):
        # code here 
        if N <= 1:
            return 0  # 1 is not considered a perfect number
        
        # Initialize the sum of factors to 1 (1 is always a factor)
        factor_sum = 1
        
        # Iterate through all possible factors up to the square root of N
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factor_sum += i  # Add the factor
                if i != N // i:  # If it's not a perfect square, add its pair factor
                    factor_sum += N // i
        
        # Check if the sum of factors is equal to N
        if factor_sum == N:
            return 1  # It's a perfect number
        else:
            return 0  # It's not a perfect number


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends