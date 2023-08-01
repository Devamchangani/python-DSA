#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while (j < k):
                if (arr[i]+arr[j]+arr[k]<0):
                    j += 1
                elif (arr[i]+arr[j]+arr[k]>0):
                    k -= 1
                else:
                    return 1
        return 0

        
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends