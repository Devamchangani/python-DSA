# class Solution:
#     def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
#         # code here
#         maxn = max(arr) 
#         l = [0] * maxn
#         for i in range(n):
#             a = arr[i]
#             print(a)
#             arr[a] += 1
#         print(l)



from typing import List


class Solution:
    def isFrequencyUnique(self, n, a):
        primer = {}
        sieve = set()
        
        for i in range(n):
            if a[i] in primer:
                primer[a[i]] += 1
            else:
                primer[a[i]] = 1
        
        for x in primer.items():
            if x[1] in sieve:
                return False
            sieve.add(x[1])
        
        return True



#{ 
 # Driver Code Starts

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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isFrequencyUnique(n, arr)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends