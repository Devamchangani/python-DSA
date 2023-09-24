class Solution:
    def duplicates(self, arr, n): 
    	# code here
        dict1 = {}
        l = []
        for i in arr:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in dict1:
            if dict1[i] >= 2:
                l.append(i)

        if len(l) == 0:
            l.append(-1)
        l.sort()
        return l


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends