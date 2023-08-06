#User function Template for python3
from itertools import permutations
class Solution:
    def permutation(self,s):
        l = len(s)
        string = list(s)
        permu = permutations(string, l)
        per = []
        for i in list(permu):
            per.append("".join(i))
        per.sort()
        return per


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends