import time
import random


# def value():
#     n=int(input("Enter the size of array:"))
#     a=[]
#     for i in range(0,n):
#         a.append(random.randint(0,100000))
#     return a

def counting_sort(array):
    size = len(array)
    output = [0]*size
    k=max(array)+1
    count = [0]*k
    for i in range(0, size):
        count[array[i]]+=1
    
    for i in range(1,k):
        count[i] += count[i-1]

    i=size-1
    while i>=0:
        output[count[array[i]]-1] = array[i]
        count[array[i]]-=1
        i-=1

    for i in range(0,size):
        array[i]=output[i]
    
    
if __name__ == "__main__":
    n=int(input("Enter the size of array:"))
    a=[]
    #Best Case:
    for i in range(0,n):
        a.append(i)
    #Worst case:
    for i in range(n,0,-1):
        a.append(i)
    #Average Case:
    for i in range(100000):
        a.append(random.randint(0,100000))
    
    t=time.time()
    counting_sort(a)
    t=time.time()-t
    print(a)
    print("time is ",t)