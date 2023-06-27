from collections import deque


#Graph input
def graph():
    g={}
    n=int(input("Enter the total number of nodes:"))
    for i in range(n):
        node=input("Enter the name of node {}:".format(i))
        a_nodes=(input("Enter values of adjacent nodes(separated by comma)for node {}:".format(node)))
        a_nodes=a_nodes.split(',')
        g[node]=a_nodes
    return g


#DFS
def dfs(graph,s,x,visited=None,path=None):
    if visited is None:
        visited=set()
    visited.add(s)
    if s==x:
        if path is None:
            path=[s]
        return path
    if path is None:
        path=[]
    path.append(s)

    for i in graph[s]:
        if i not in visited:
            res=dfs(graph,i,x,visited,path.copy())
            if res is not None:
                return res
    return None


#BFS
def bfs(graph,s,x):
    visited=set()
    queue=deque([(s,[s])])
    while queue:
        node,path = queue.popleft()
        if node == x:
            return path
        if node not in visited:
            visited.add(node)
            for a in g[node]:
                if a not in visited:
                    queue.append((a,path+[a]))

    return "Not Found!"

def traverse():
    ch=0
    while(ch!=3):
        print(" 1).DFS \n 2).BFS \n 3).EXIT")
        ch=int(input("Enter Your Choice:"))
        if ch==1:
            s=input("Enter the starting node:")
            x=input("Enter the node you want to search:")
            pos=dfs(g,s,x)
            if pos:
                print("The path is:\t",'\t-->\t'.join(pos))
            else:
                print("The node is not found!!!")
        if ch==2:
            s=input("Enter the starting node:")
            x=input("Enter the node you want to search:")
            pos=bfs(g,s,x)
            if pos:
                print("The path is:\t",'\t-->\t'.join(pos))
            else:
                print("The node is not found!!!")
        if ch==3:
            print("Exited Successfully !!!")
            exit(0)



if __name__ == "__main__":
    g=graph()
    print("Graph :",g)
    traverse()


