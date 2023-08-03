#User function Template for python3
import heapq
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            z = edges[i][2]
            adj[u].append((v, z))
        dist = [float('inf')] * n
        dist[0] = 0
        pq = []
        heapq.heappush(pq, (0, 0))
        while pq:
            weight, node = heapq.heappop(pq)
            if weight > dist[node]:
                continue
            for adjNode, weightage in adj[node]:
                if weight + weightage < dist[adjNode]:
                    dist[adjNode] = weight + weightage
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist


#{ 
 # Driver Code Starts
# 6 7
# 0 1 2
# 0 4 1
# 4 5 4
# 4 2 2
# 1 2 3
# 2 3 6
# 5 3 1
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends