#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        # print(s1,s2)
        i1 = int(s1)
        i2 = int(s2)
        return str(i1*i2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends

