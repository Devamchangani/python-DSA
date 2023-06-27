import time
import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

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
    radix_sort(x)
    t=time.time()-t
    print("Time required : ",t)
    print(x)