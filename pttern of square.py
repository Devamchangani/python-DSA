#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def square(s):
    #Complete the code given below
    # Replace the .... by your own code
    for i in range(s):
        if i == 0 :
            for i in range(s):
                print("*", end=" ")
                # print("")
            print("")

        elif i == s-1:
            for i in range(s):
                print("*", end=" ")

        else:
            for i in range(s):
                if i == 0 or i == s-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("")
            
    print("")


# second method
    for i in range(s):
        for j in range(s):
            if i == 0 or i == s-1 or j == 0 or j == s-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("") 

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=int(input())
        square(s)
        
# } Driver Code Ends