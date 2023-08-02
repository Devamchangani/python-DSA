#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


def avg(mylist):
    ##Your Code Here
    min_val = min(mylist)
    max_val = max(mylist)

    # Remove one occurrence of the minimum and maximum values
    mylist.remove(min_val)
    mylist.remove(max_val)
    
    total_sum = sum(mylist)

    # Calculate the number of elements in the list (excluding the minimum and maximum values)
    num_elements = len(mylist)

    # Calculate the average and return the integer division (floor)
    average = total_sum // num_elements
    return average

#{ 
 # Driver Code Starts.




def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        
        mylist = [int(x) for x in input().split()]
        print(avg(mylist))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends