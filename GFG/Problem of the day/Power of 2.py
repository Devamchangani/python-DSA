#User function Template for python3
class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        #Your code here
        
# MORE TIME TAKEN BY THIS METHOD
        # for i in range(n):
        #     # if pow(2,i) == n:
        #     #     return True
        #     n = n//2

# LESS TIME TAKEN BY THIS METHOD
        
        return (x and (not(x & (x - 1))))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends