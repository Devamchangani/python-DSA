#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

    
def nearestPower(A, B):
    ##Your code here
    ##return the closest power
    P = 1
    min_diff = float('inf')
    closest_power = 0

    while True:
        X = A ** P
        diff = abs(X - B)

        if diff < min_diff:
            min_diff = diff
            closest_power = X

        if X >= B:
            break

        P += 1

    return closest_power


#{ 
 # Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(nearestPower(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends