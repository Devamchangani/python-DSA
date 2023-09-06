def size():
    l = []
    n = int(input("Enter a Number size: "))
    for i in range(n): 
        s = int(input("Enter sender 0 or 1 only: "))
        l.append(s)
    return l,n

#-------------------partition of list----------------------
def saprate_list(l,n):
    l_1 = []

    if n%3 == 0:
        size = 3
    elif n%4 == 0:
        size = 4
    elif n%5 == 0:
        size = 5
    else:
        print("not allow a prime number")

    # -------saprate a list in 5 size-----

    for i in range(0, len(l), size):
        l_1.append(l[i:i+size])
    print(l_1)
    return l_1


#----------------addition of all list------------------------ 
def addition_list(l_1):
    sen = []
    for j in range(0, len(l_1[0])):
        tmp = 0
        for i in range(0, len(l_1)):
            tmp = tmp + l_1[i][j]
        sen.append(tmp)
    return sen

#-----------------------------Row parities----------------------- 
def row_parities(sen):
    send = []
    for i in range(len(sen)):
        if(sen[i] %2 == 0):
            send.append(0)
        else:
            send.append(1)
    l_1.append(send)
    return l_1

# ---------------Addition of all sub list-------------
def addition_sublist(l_1):
    l_2 = []
    for i in range(0, len(l_1)):
      tmp = 0
      for j in range(0, len(l_1[i])):
        tmp = tmp + l_1[i][j]
      l_2.append(tmp)
    return l_2

# ------------------Add row parity-----------------
def check_add_parities(l_2):
    # l_2 = []
    for i in range(0, len(l_2)):
        if(l_2[i] % 2 == 0):
            l_1[i].append(0)
        else:
            l_1[i].append(1)

    print(l_1)
    return l_1

def compare(send,recv):
    if(send == recv):
        print("Accepted")
    else:
        print("rejected")
        print("please try to send again")

if __name__ == "__main__":

    # l = []
    # l_1 = []
    # sen = []
    # send = []
    # l_2 = []
    
# ------------sender-------------
    l,n = size()
    print(l)
    l_1 = saprate_list(l,n)
    sen = addition_list(l_1)
    l_1 = row_parities(sen)
    l_2 = addition_sublist(l_1)
    sender = check_add_parities(l_2)
    

# ----------reciver-----------------
    l,m = size()
    print(l)
    l_1 = saprate_list(l,n)
    sen = addition_list(l_1)
    l_1 = row_parities(sen)
    l_2 = addition_sublist(l_1)
    reciver = check_add_parities(l_2)
    
    
    compare(sender, reciver)