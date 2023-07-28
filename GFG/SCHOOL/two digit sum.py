#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def digitsSum(N):
    ##Your code here
    t = N//10
    s = N % 10
    sum = t + s
    return sum
    

#{ 
 # Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(digitsSum(N))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends