#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def realSum(mylist):
    ##Your code here
    total_sum = 0
    skip_next = False

    for i in range(len(mylist)):
        if skip_next:
            skip_next = False
            continue

        if mylist[i] == 7:
            skip_next = True
            continue

        total_sum += mylist[i]

    return total_sum
            


#{ 
 # Driver Code Starts.




def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        
        mylist = [int(x) for x in input().split()]
        print(realSum(mylist))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends