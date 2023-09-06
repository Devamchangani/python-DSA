import heapq
def cookies(k, A):
    # Write your code here
    h=[i for i in A]
    heapq.heapify(h)
    ans=0
    while h[0]<k and len(h)>1:
        f=heapq.heappop(h)
        s=heapq.heappop(h)
        heapq.heappush(h,f+2*s)
        ans+=1
        
    if h[0]>=k:
        return ans
    else:
        return -1
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    print(result)