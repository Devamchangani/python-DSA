#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    # def deleteMid(self, s, sizeOfStack):
    #     # code here
    def deleteMid(self, s, sizeOfStack):
    # Check if stack size is less than 2
        if sizeOfStack < 2:
            return s
    
        mid = (sizeOfStack + 1) // 2
        self.deleteMiddleUtil(s, sizeOfStack, mid)

    def deleteMiddleUtil(self, s, sizeOfStack, mid):
    # Base case: If stack is empty or middle element is reached
        if sizeOfStack == mid:
            s.pop()
            return
    
    # Remove current top element
        temp = s.pop()
        
    # Recur for the remaining stack
        self.deleteMiddleUtil(s, sizeOfStack - 1, mid)
    
    # Push the popped element back into the stack
        s.append(temp)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends