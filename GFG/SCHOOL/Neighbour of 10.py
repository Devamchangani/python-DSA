#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def isNeighbour(N):
    ##Your code here
    if N >= 3:
        a = N % 10
        if (10-a)<=2 or a<=2:
            # print("Is Neighbour")
            return True
        else:
            # print("Not neighbour")
            return False
    else:
        # print("Not neighbour")
        return False



#{ 
 # Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(isNeighbour(N))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends