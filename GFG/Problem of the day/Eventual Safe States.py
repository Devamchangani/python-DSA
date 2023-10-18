#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        def isSafe(node):
        # If this node is already visited, it is safe.
            if visited[node] == 1:
                return True
            # If this node is being visited, we've detected a cycle, and it's not safe.
            if visited[node] == -1:
                return False
            visited[node] = -1  # Mark the node as being visited.
            for neighbor in adj[node]:
                if not isSafe(neighbor):
                    return False
            visited[node] = 1  # Mark the node as visited and safe.
            return True
    
        visited = [0] * V  # 0 represents unvisited, -1 represents being visited, 1 represents visited and safe.
        safe_nodes = []
    
        for node in range(V):
            if isSafe(node):
                safe_nodes.append(node)
    
        return sorted(safe_nodes)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends