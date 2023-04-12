import time
def inp():
    l = []
    n = int(input("Enter the total size : "))
    for i in range(n):
        a = int(input())
        l.append(a)
    print(l)
    return l


def linear_serch(l,e):
    flag = 0
    for i in range(len(l)):
        if e == l[i]:
            flag = 1
            break
        else:
            flag = 0
        
    if(flag == 1):
        print(f"FOUND AT INDEX OF {i+1}")
    else:
        print("NOT FOUND")



def binary_serch(l,low,high,e):
 
    while low <= high:
 
        mid = low + (high - low) // 2
 
        
        if l[mid] == e:
            return mid+1
        elif l[mid] < e:
            low = mid + 1
        else:
            high = mid - 1
 
    return -1


def bubble(l1):
    for i in range(0,len(l1)-1):
        for j in range(len(l1)-1):  
            if l1[j] > l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp

    return l1

if __name__ == "__main__":

    l = inp()
    e = int(input("Enter the serch element : "))


# AVRAGE LINEAR SERCH
    st1 = time.time()
    linear_serch(l, e)
    et1 = time.time()
    tt1 = et1 - st1




# BEST LINEAR SERCH

    l.remove(e)
    l.insert(0,e)

    st = time.time()
    linear_serch(l, e)
    et = time.time()
    tt = et - st


# WORST LINEAR SERCH

    l.remove(e)
    l.append(e)

    st2 = time.time()
    linear_serch(l, e)
    et2 = time.time()
    tt2 = et2 - st2


# -------------------------------------BINARY SEARCH----------------------
    print(" ")
    print("++++++++++++++++BINARY SEARCH++++++++++++++++++")
    l = bubble(l)
    print(l)
# AVRAGE BINARY SERCH

    
    
    st3 = time.time()
    flag = binary_serch(l, 0, len(l)-1, e)
     
    if(flag != -1):
        print(f"FOUND AT INDEX OF {flag}")
    else:
        print("NOT FOUND")
    et3 = time.time()
    tt3 = et3 - st3


# BEST BINARY SERCH

    
    e = l[len(l)//2]
    # print(e)
    st4 = time.time()
    flag = binary_serch(l, 0, len(l)-1, e)
     
    if(flag != -1):
        print(f"FOUND AT INDEX OF {flag}")
    else:
        print("NOT FOUND")
    et4 = time.time()
    tt4 = et4 - st4



# WORST BINARY SERCH

    
    e = max(l)
    # print(e)
    st5 = time.time()
    flag = binary_serch(l, 0, len(l)-1, e)
     
    if(flag != -1):
        print(f"FOUND AT INDEX OF {flag}")
    else:
        print("NOT FOUND")
    et5 = time.time()
    tt5 = et5 - st5


    print("")
    print(f"linear serch avrage time : {tt}")
    print(f"linear serch avrage time : {tt1}")
    print(f"linear serch worst time : {tt2}")
    print(f"binary serch worst time : {tt3}")
    print(f"binary serch worst time : {tt4}")
    print(f"binary serch worst time : {tt5}")