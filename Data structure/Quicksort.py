import random
import time


def random_list():
  n = int(input("Enter a Number size: "))
  for i in range(n):
    l1.append(random.randrange(0,n))
    
  print(f"MAIN LIST :- {l1}")
  return l1



def particion(l1,low,high):
    pivot = l1[high]
    i = low - 1


    for j in range(low,high):
        if(l1[j] <= pivot):
            i = i + 1

            (l1[i], l1[j]) = (l1[j], l1[i])

    (l1[i + 1], l1[high]) = (l1[high], l1[i + 1])


    return i + 1


def quick(l1,low,high):
    
    if(low < high):
        part = particion(l1, low, high)
        quick(l1, low, part - 1)
        quick(l1, part + 1, high)

if __name__ == "__main__":
    l1 = []
    l1 = random_list()


    
# Best case
    st = time.time()
    quick(l1, 0, len(l1)-1)
    et = time.time()
    tt = et - st
    print(l1)

# worst case
    st1 = time.time()
    quick(l1, 0, len(l1)-1)
    et1 = time.time()
    tt1  = et1 - st1
    print(l1)

# avrage case
    l1 = l1[::-1]  #reverse the list
    print(l1)


    st2 = time.time()
    quick(l1, 0, len(l1)-1)
    et2 = time.time()
    tt2  = et2 - st2
    print(l1)

    print(f"Best cassetime: {tt}")
    print(f"avrage cassetime: {tt2}")
    print(f"wrost cassetime: {tt1}")
   