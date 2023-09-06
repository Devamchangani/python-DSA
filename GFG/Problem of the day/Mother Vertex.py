
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		visited = [False] * V
        mv = -1
        for i in range(V):
            if not visited[i]:
                self.dfs(adj, i, visited)
                mv = i
        visited = [False] * V
        self.dfs(adj, mv, visited)
        for v in visited:
            if not v:
                return -1
        return mv
        
    def dfs(self, adj, i, visited):
        visited[i] = True
        for x in adj[i]:
            if visited[x]:
                continue
            self.dfs(adj, x, visited)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends