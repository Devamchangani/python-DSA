# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words = S.split('.')
    
    # Reverse the list of words
        reversed_words = words[::-1]
    
    # Join the reversed words using the delimiter '.'
        return '.'.join(reversed_words)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends