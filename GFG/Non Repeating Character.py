#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here

# USING DICTIONARY
        # char = {}
        # l = len(s)
        # # print(l)
        # for i in range(l):
        #     if s[i] not in char:
        #         char[s[i]] = 1
        #     else:
        #         char[s[i]] += 1


        # for key, val in char.items():
        #         if val == 1:
        #             # keys_list.append(key)
        #             ans = key
        #             break
        #         else:
        #             ans = "$" 
        # return ans

        for i in s:
            count = 0
            for j in s:
                if i == j:
                    count+=1
                if count > 1:
                    break
            if count == 1:
                return i
                break

        return "$"
    
    

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# } Driver Code Ends