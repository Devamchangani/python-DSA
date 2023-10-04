#User function Template for python3
import roman
class Solution:
    
    def rto(self, a):
        switch = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        return switch.get(a, -1)


    def romanToDecimal(self, S): 
        # code here
        # return roman.fromRoman(S)
        n = len(S)
        ans = 0
        for i in range(n):
            if i < n-1 and self.rto(S[i]) < self.rto(S[i+1]):
                ans -= self.rto(S[i])
            else:
                ans += self.rto(S[i])
        return ans

    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends