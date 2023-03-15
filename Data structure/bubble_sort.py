import random
import time


def random_list():
    n = int(input("Enter a Number size: "))
    for i in range(n):
        l1.append(random.randrange(0,n))
        # l.append(random.randrange(0,n))

    print(f"MAIN LIST :- {l1}")
    return l1

# This function used to creat asscending order list
def bubble(l1):
    for i in range(0,len(l1)-1):
        for j in range(len(l1)-1):  
            if l1[j] > l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp

    return l1


# This function used to creat dicending order list
def bubble2(l1):
    for i in range(0,len(l1)-1):
        for j in range(len(l1)-1):  
            if l1[j] < l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp
    return l1




if __name__ == "__main__":
    l1 = []
    # l = []


    l1 = random_list()

# avrage case
    st = time.time()
    l1 = bubble(l1)
    et = time.time()
    tt  = et - st
    print(l1)

    # best case
    st1 = time.time()
    bubble(l1)
    et1 = time.time()
    tt1  = et1 - st1
    print(l1)

    # wrost case
    l1 = bubble2(l1)
    print(l1)
    st2 = time.time()
    bubble(l1)
    et2 = time.time()
    print(l1)
    tt2  = et2 - st2


    print(f"Best cassetime: {tt1}")
    print(f"Avrage cassetime: {tt}")
    print(f"Wrost cassetime: {tt2}")