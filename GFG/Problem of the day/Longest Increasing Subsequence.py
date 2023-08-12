#User function Template for python3
import bisect
class Solution:
    
    #Function to find length of longest increasing subsequence.
    # def longestSubsequence(self,a,n):
    #     # code here
    #     dp = []
    #     dp.append(a[0])
    #     for i in range(1,n):
    #         if a[i] > dp[-1]:
    #             dp.append(a[i])
    #         else:
    #             it = bisect.bisect(dp, a[i])
    #             dp[it] = a[i]
    #     return len(dp)

    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        piles = []  # Store the top elements of piles
        for a in a:
            # Find the index where the current number should be inserted in the piles
            pile_index = bisect.bisect_left(piles, a)
            
            # If the index is equal to the number of piles, it means we're starting a new pile
            if pile_index == len(piles):
                piles.append(a)
            else:
                piles[pile_index] = a  # Replace the top element of the pile
            
        return len(piles)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends