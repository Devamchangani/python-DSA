#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to check if pair 
# with given sum exists
def pair_sum(dict, N, arr, sum):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    for x in arr:
        diff = sum - x
        # Check if the difference exists in the dictionary and its frequency is greater than zero
        dict[x] -= 1
        if diff in dict and dict[diff] > 0:
            # if dict[diff] == 1:
            #     return False
            return True
    
    return False

#{ 
 # Driver Code Starts.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        N = int(input())
        sum = int(input())
        dict = {}
        x = N
        arr = [int(i) for i in (input().split())]
        
        for i in arr:
            dict[i] = 0
                
        for i in arr:
            dict[i] +=1
    
        if pair_sum(dict, N, arr, sum) is True:
            print ("Yes")
        else:
            print ("No")
        
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends