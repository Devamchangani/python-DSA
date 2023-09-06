#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def triangleWall(s):
    
    #Complete the given code
    #Replace .... by your own code
    for i in range(1,s+1):
        for j in range(i):
            print("*", end=" ")
        print("")
        
    
    print("")

    for i in range(1,s+1):
        for j in range(i):
            # if i == 2:
            #     print("* ", end=" ")
            if j == 0 or j == i-1 or i == s:
                print("* ", end=" ")
            else:
                print("   ", end=" ")
        print("")
#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=int(input())
        triangleWall(s)
# } Driver Code Ends