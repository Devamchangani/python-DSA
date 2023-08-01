#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        t = S[::-1]
        n = len(S)
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if S[i - 1] == t[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur.copy()
        return prev[n]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends