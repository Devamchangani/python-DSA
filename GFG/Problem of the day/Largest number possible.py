#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        if S == 0:
            if N == 1:
                return 0
            else:
                return -1
    
        if S > 9 * N:
            return -1
    
        largest_number = [0] * N
    
        for i in range(N):
            digit = min(9, S)
            largest_number[i] = digit
            S -= digit
    
        return int(''.join(map(str, largest_number)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends