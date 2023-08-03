#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to print elements in sorted order
def sorted_elements(arr):
    l = []
    # Your code here
    # return the list which contains 
    # elements in sorted order
    
    for i in arr:
        if int(i) not in l:
            l.append(int(i))
    l.sort()
    return l


#{ 
 # Driver Code Starts.
# Driver Code
def main():
    testcase = int(input())
    
    while testcase > 0:
        arr = input().split()
        l = sorted_elements(arr)
        
        for x in l:
            print (x, end = ' ')
        
        print ()
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends