#User function Template for python3

class Solution:
    def reverseWord(self, s):
        return s[::-1]

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends