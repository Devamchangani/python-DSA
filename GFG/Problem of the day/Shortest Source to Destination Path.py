#User function Template for python3
from collections import deque

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0] == 0:
            return -1

        queue = deque([(0, 0, 0)])
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[0][0] = True

        while queue:
            x, y, dist = queue.popleft()

            if x == X and y == Y:
                return dist

            # Possible moves: up, down, left, right
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < N and 0 <= new_y < M and A[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    queue.append((new_x, new_y, dist + 1))
                    visited[new_x][new_y] = True

        return -1

#{ 
 # Driver Code Starts
# 3 4
# 1 0 0 0 
# 1 1 0 1 
# 0 1 1 1
# 2 3
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends