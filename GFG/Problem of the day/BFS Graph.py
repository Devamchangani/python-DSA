#User function Template for python3

from typing import List
from queue import Queue
from collections import deque

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        bfd_trav = []
        visited = [False] * V
        queue = deque()
        visited[0] = True
        queue.append(0)

        while queue:
            vertex = queue.popleft()
            bfd_trav.append(vertex)

            for adj_ver in adj[vertex]:
                if not visited[adj_ver]:
                    visited[adj_ver] = True
                    queue.append(adj_ver)

        return bfd_trav
#{ 
 # Driver Code Starts
# 5 4
# 0 1 
# 0 2
# 0 3 
# 2 4
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends