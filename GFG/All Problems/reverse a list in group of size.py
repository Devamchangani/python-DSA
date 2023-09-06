def rev(data,k):
    # dict = {}
    l = len(data)
    a = []
    print("")
    for i in range(0,l,k):
        for j in range(i,i+k):
            if j < l:
                a.insert(i, data[j])
            else:
                break
    print(a)



if  __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        data = [str(x)for x in input("Enter the data: ").split()]
        k = int(input())
        rev(data,k)
        tc -= 1