#User function Template for python3

class Solution:
    #Function to return a list containing the intersection of two arrays.
    def printIntersection(self,a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return: array of intersection of two array or -1
        '''
        # code here
        # This code more time taken
        # inte = []
        # for i in a:
        #     if i in b:
        #         inte.append(i)
        # return inte


        # This code less time taken
        intersection = []
        i = 0
        j = 0
    
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                # If the elements are equal, add to the intersection list
                if not intersection or intersection[-1] != a[i]:
                    intersection.append(a[i])
                i += 1
                j += 1
    
        if not intersection:
            intersection.append(-1)
    
        return intersection

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        l = ob.printIntersection(a,b,n,m)
        print(*l)
# } Driver Code Ends