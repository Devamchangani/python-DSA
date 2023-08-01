#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        shift = segregate(arr, n)

        # Consider only positive numbers
        positive_arr = arr[shift:]

        # Mark positive numbers as visited
        for i in range(len(positive_arr)):
            num = abs(positive_arr[i])
            if num - 1 < len(positive_arr):
                positive_arr[num - 1] = -abs(positive_arr[num - 1])

        # Find the first index with a positive number
        for i in range(len(positive_arr)):
            if positive_arr[i] > 0:
                return i + 1

        # If all positive numbers are present, the answer is n+1
        return len(positive_arr) + 1

def segregate(arr, n):
    shift = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i], arr[shift] = arr[shift], arr[i]
            shift += 1
    return shift    
#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends