#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        char = {}
        char1 = {}
        for c in a:
            if c not in char:
                char[c] = 1
            else:
                char[c] += 1

        for c in b:
            if c not in char1:
                char1[c] = 1
            else:
                char1[c] += 1


        if char == char1:
            return True
        else:
            return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends