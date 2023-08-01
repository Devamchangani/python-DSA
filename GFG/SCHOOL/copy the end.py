#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3



def copyCat(str):
    ##Your code here
    end = ''
    if len(str) >= 2:
        l = str[len(str)-2:]
        for i in range(3):
            end += l
    return end

#{ 
 # Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(copyCat(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends