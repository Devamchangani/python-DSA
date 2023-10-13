#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        floor_value = -1  # Initialize floor_value to -1

        while root is not None:
            if root.data == x:
                return root.data
            elif root.data < x:
                # If the current node's value is less than or equal to x, update floor_value and move to the right subtree.
                floor_value = root.data
                root = root.right
            else:
                # If the current node's value is greater than x, move to the left subtree.
                root = root.left
    
        return floor_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends