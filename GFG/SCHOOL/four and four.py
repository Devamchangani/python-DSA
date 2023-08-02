#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


def has44(arr):
    ##Your code here
    for i in range(len(arr) - 1):
        if arr[i] == 4 and arr[i + 1] == 4:
            return True
    return False


#{ 
 # Driver Code Starts.




def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        
        arr = [int(x) for x in input().split()]
        print(has44(arr))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends