#User function Template for python3


def imgExtracter(str):
    ##Your code here
    #Print the output
    pattern = r"src='(.*?\.jpg)'"
    match = re.search(pattern, str)
    if match:
        image_url = match.group(1)
        print(image_url)
    else:
        print("Image URL not found.")
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import re

# <html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html>



def main():
    testcases=int(input()) #testcases
    while(testcases > 0):
        str = input()
        imgExtracter(str)
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends