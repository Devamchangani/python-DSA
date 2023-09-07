#User function Template for python3
import queue
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0
        visited = [0] * 100000
        q = queue.Queue()
        count = 0
        q.put(start)
        visited[start] = True
        while not q.empty():
            size = q.qsize()
            while size > 0:
                num = q.get()
                size -= 1
                if num == end:
                    return count
                for change in arr:
                    changedNum = (num * change) % 100000
                    if not visited[changedNum]:
                        visited[changedNum] = 1
                        q.put(changedNum)
            count += 1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends