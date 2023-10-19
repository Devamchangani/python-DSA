#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        visited = [False] * V
        level = [-1] * V
    
        # Mark the starting node as visited and set its level to 0.
        visited[0] = True
        level[0] = 0
    
        # Create a queue for BFS and enqueue the starting node.
        queue = deque()
        queue.append(0)
    
        # Perform BFS traversal.
        while queue:
            node = queue.popleft()
    
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[node] + 1
                    queue.append(neighbor)
    
                    # If the current neighbor is the node labeled as X, return its level.
                    if neighbor == X:
                        return level[X]
    
        # If node X is not found, return -1.
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends