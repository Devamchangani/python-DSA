#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        if not arr or not brr:
            return None, None
        
        arr.sort()
        brr.sort()
        
        closest_pair = None
        min_distance = float('inf')
        
        i = 0  # Pointer for arr
        j = m - 1  # Pointer for brr
        
        while i < n and j >= 0:
            pair_sum = arr[i] + brr[j]
            distance = abs(pair_sum - x)
            
            if distance < min_distance:
                min_distance = distance
                closest_pair = (arr[i], brr[j])
            
            # Move pointers based on the comparison with x
            if pair_sum < x:
                i += 1
            else:
                j -= 1
        
        return closest_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends