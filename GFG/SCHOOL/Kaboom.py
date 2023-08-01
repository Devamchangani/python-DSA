#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def boom(str):
    ##Your code here
    print(str[-4:])
    if str[-4:] == "boom":
        return True
    else:
        return False


#{ 
 # Driver Code Starts.





def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        str = input()
        print(boom(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends