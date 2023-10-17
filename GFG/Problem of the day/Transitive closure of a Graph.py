#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        for self in range(N):
            graph[self][self] = 1
        for via in range(N):
            for from_ in range(N):
                for to in range(N):
                    graph[from_][to] |= (graph[from_][via] & graph[via][to])
        return graph


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends