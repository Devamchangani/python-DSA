#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def cat_hat(str):
    c,h = 0,0

    for i in range(0,len(str)):
        print(str[i:i+3])
        if str[i:i+3] == 'cat':
            c += 1
        if str[i:i+3] == 'hat':
            h += 1

    # print(c,h)
    if c == h:
        return True
    else:
        return False
    

#{ 
 # Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends