#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        l2 = []
        #code here
        # More time taken
        # for i in range(n):
        #     if a[i] not in l2:
        #         l2.append(a[i])
        # for j in range(m):
        #     if b[j] not in l2:
        #         l2.append(b[j])

        # Less time taken 
        l2 = list(set(a) | set(b))
        return len(l2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends