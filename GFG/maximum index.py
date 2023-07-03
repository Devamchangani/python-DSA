#User function Template for python3
class Solution:
    def maxIndexDiff(self, arr, n):
        left = [0] * n
        right = [0] * n
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = min(arr[i], left[i-1])
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if left[i] <= right[j]:
                ans = max(ans, j-i)
                j += 1
            else:
                i += 1
        return ans



#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends