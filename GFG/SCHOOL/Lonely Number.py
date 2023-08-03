#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
from collections import Counter
# Function to print elements in sorted order
def find_lonely(numbers, K):
    # Your code here
    dict = Counter(numbers)
    n = False
    for num, count in dict.items():
        if count == K:
            # print(num)
            continue
        else:
            n = True
            m = num

    
    if n == True:
        print(m)
    else:
        print(-1)

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    testcase = int(input())
    
    while testcase > 0:
        K = int(input())
        numbers = input().split()
        find_lonely(numbers, K)
        
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends