import time
import random

def bucket_sort(arr):
    n = len(arr)
    k = max(arr) + 1
    
    buckets = [[] for _ in range(k)]
    
    for i in range(n):
        bucket_idx = arr[i]
        buckets[bucket_idx].append(arr[i])

    for i in range(k):
        insertion_sort(buckets[i])
        
    index = 0

    for i in range(k):
        for j in range(len(buckets[i])):
            arr[index] = buckets[i][j]
            index += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    n=int(input("Enter the size of array:"))
    x=[]
    
    #Best Case:
    for i in range (n):
        x.append(i)
    
    #Worst case:
    for i in range(n,0,-1):
        x.append(i)
    
    #Average Case:
    for i in range(n):
        x.append(random.randint(0,n))
    
    t=time.time()
    bucket_sort(x)
    t=time.time()-t
    print(t)
