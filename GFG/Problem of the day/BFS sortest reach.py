#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import defaultdict, deque
def bfs(n, m, edges, s):
    # Write your code here
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = [-1] * n
    distances[s-1] = 0

    queue = deque([s])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor-1] == -1:
                distances[neighbor-1] = distances[node-1] + 6
                queue.append(neighbor)

    distances.pop(s-1)
    return distances

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        print(result)