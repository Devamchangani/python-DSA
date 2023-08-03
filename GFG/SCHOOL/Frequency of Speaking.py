#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to count frequency of words
def frequency_word(statement):
    
    # Your code here
    dict = {}
    for i in statement:
            dict[i] = 0
                
    for i in statement:
        dict[i] +=1

    for i in dict:
        if dict[i] > 1:
            print(i, dict[i])
        else:
            print(i)
    print(dict)
#{ 
 # Driver Code Starts.
# Driver Code this is the man who did this task which is the task to be done by another man
def main():
    # testcase input
    testcase = int(input())
    
    # loop to iterate through testcases
    while testcase > 0:
        statement = input().split()
        frequency_word(statement)
        
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends