#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        # # code here
        # mask = 1
        # if l<1 or r>32:
        #     return x
        
        # if x > y:
        #     for i in range(l, r+1):
            
        #         mast = 1 << (i -1)
        #         if i >= y:
        #     # if((y and mask) != 0):
        #         # x = x | mask
        #             x += 1
        
        # return x            
        mask = ((1 << (r - l + 1)) - 1) << (l - 1)
        setBits = y & mask
        x = x | setBits
        return x
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends