#Time analysis of 0/1 Knapsack Problem using Dynamic Programming
import time

def value():
    n=int(input("Enter the no of object:"))
    w=[int(x) for x in input("Enter the weights of objects separated by space:").split()]
    v=[int(x) for x in input("Enter the values of objects separated by space:").split()]
    c=int(input("Enter the maximum capacity of knapsack:"))
    return n,w,v,c

def knapsack_01(v,w,c,n):
    if(n==0 or c==0):
        return 0
    if(w[n-1]>c):
        return knapsack_01(v,w,c,n-1)
    else:
        return max(v[n-1]+knapsack_01(v,w,c-w[n-1],n-1),knapsack_01(v,w,c,n-1))



if __name__ == "__main__":

    n,w,v,c = value()

    s=time.time()
    print("Start time:",s)
    p=knapsack_01(v,w,c,n)
    e=time.time()

    print("Calculated profit is :",p)
    print("End time:",e)
    print("Time complexity for 0/1 knapsack using dynamic programing:",e-s)