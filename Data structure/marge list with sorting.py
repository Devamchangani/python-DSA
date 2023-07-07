# User function Template for python3

class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # i = 0
        # j = 0
        # k = n - 1

        # while i < k:
        #     while (arr1[i] > arr2[j]):
        #         (arr1[k],arr2[j]) = (arr2[j],arr1[k])
        #         j += 1
        #         k -= 1
        #     i += 1
        # arr1.sort()
        # arr2.sort()
        # # return arr1, arr2
    
        arr3 = arr1 + arr2
        arr3.sort()
        print(arr3)
        arr1.clear()
        arr2.clear()

        print(arr1,arr2)
        for i in range((n+m)):
            a = arr3[i]
            if i<n:
                arr1.append(a)
            else:
                arr2.append(a)
            # arr1[i] = arr3[i]
            # arr3.pop(i)

        print(arr1)
        print(arr2)

        # while n >= 0:
        #     arr1[i] = arr3[j]
        #     i += 1
        #     j += 1
        #     n -= 1


        # print(arr1)


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n, m = map(int, input().strip().split())
        # arr1 = list(map(int, input().strip().split()))
        # arr2 = list(map(int, input().strip().split()))
        arr1 = [2, 85, 45, 32]
        arr2 = [0, 99, 55, 25, 28]
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
# } Driver Code Ends
