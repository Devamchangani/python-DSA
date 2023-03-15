import random
import time


def random_list():
  n = int(input("Enter a Number size: "))
  for i in range(n):
    l1.append(random.randrange(0,n))
    
  print(f"MAIN LIST :- {l1}")
  return l1

# This function used to creat asscending order list
def insertion(l1):
    for j in range(len(l1)):
        key = l1[j]
        i = j - 1
        while(i >= 0 and l1[i] > key):
            l1[i+1] = l1[i]
            i = i - 1
        l1[i+1] = key
    # print(l1)


# This function used to creat dicending order list
def selection2(l1):
  for i in range(len(l1)):
    for j in range(len(l1)):
      if(l1[i] > l1[j]):
        temp = l1[i]
        l1[i] = l1[j]
        l1[j] = temp
  return l1


if __name__ == "__main__":
    l1 = []
    l1 = random_list()


    # avrage case
    st = time.time()
    insertion(l1)
    et = time.time()
    tt = et - st
    print(l1)

    # best case
    st1 = time.time()
    insertion(l1)
    et1 = time.time()
    tt1  = et1 - st1
    print(l1)
  
    # wrost case
    selection2(l1) #reverse the list
    print(l1)
    
    st2 = time.time()
    insertion(l1)
    et2 = time.time()
    tt2  = et2 - st2
    print(l1)
    
    
    print(f"Best cassetime: {tt1}")
    print(f"Avrage cassetime: {tt}")
    print(f"Wrost cassetime: {tt2}")