

class Solution:
    def completeRows(self, n : int) -> int:
        # code here
        total_rows = 0
        bricks_needed = 1
        while n >= bricks_needed:
            n -= bricks_needed
            bricks_needed += 1
            total_rows += 1
        return total_rows


#{ 
 # Driver Code Starts


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.completeRows(n)
        
        print(res)
        

# } Driver Code Ends