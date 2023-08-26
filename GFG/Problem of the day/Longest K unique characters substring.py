#User function Template for python3

class Solution:

    def longestKSubstr(self, S, K):
        # code here
        if K == 0 or not S:
            return -1

        char_count = {}  # Dictionary to store character frequencies
        left = 0  # Left pointer of the sliding window
        max_length = -1  # Maximum length of substring with K unique characters
    
        for right in range(len(S)):
            char_count[S[right]] = char_count.get(S[right], 0) + 1
    
            # Shrink the window until the number of unique characters is less than K
            while len(char_count) > K:
                char_count[S[left]] -= 1
                if char_count[S[left]] == 0:
                    del char_count[S[left]]
                left += 1
    
            # Update the maximum length
            if len(char_count) == K:
                max_length = max(max_length, right - left + 1)
    
        return max_length




#{ aabacbebebe
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends