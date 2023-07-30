#{ 
 # Driver Code Starts
#Initial Template for Python 3


import re ##import re module to use regex

# } Driver Code Ends
#User function Template for python3

# numbers = re.findall('\d+',input)

#      # now we need to convert each number into integer
#      # int(string) converts string into integer
#      # we will map int() function onto all elements 
#      # of numbers list
#      numbers = map(int,numbers)

#      print max(numbers)


def numberMatcher(str):
    pat='\d+'
    match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")


#{ 
 # Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends