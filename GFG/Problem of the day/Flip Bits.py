#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        one = 0
        for i in range(n):
            if a[i] == 1:
                one += 1
                a[i] = -1
            else:
                a[i] = 1

        cursum, maxsum = 0,0
        for i in range(n):
            cursum += a[i]
            maxsum = max(maxsum,cursum)
        
            if cursum < 0:
                cursum = 0

        return one+maxsum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends