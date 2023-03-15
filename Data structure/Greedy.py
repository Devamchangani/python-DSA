# FUNCTION OF READ INPUT 
def element():
    n = int(input("Size of object: "))
    for i in range(n):
        profit = int(input("Enter the Profit: "))
        p.append(profit)
        weight = int(input("Enter the weight: "))
        w.append(weight)
        x = p[i]/w[i]
        a.append(x)


    print(f"Profit list is : {p}")
    print(f"weight list is : {w}")
    print(f"Ratio list is : {a}")


    cap = int(input("Enter the capicity: "))


    return n,cap,p,w,a



# FUNCTION OF MAXIMUM PROFIT
def largest_profit(n,cap,p,w):
    lp = 0

    for i in range(n):
        max_profit_index = p.index(max(p))
        max_profit = p[max_profit_index]
        max_weight = w[max_profit_index]


        if(max_weight <= cap):
            cap -= max_weight
            lp += max_profit
        else:
            lp += max_profit*cap/max_weight
            break


        p.remove(max_profit)
        w.remove(max_weight)


    return lp



# FUNCTION OF MINIMUM WEIGHT
def minimum_weight(n,cap,p,w):
    mw = 0
    for i in range(n):
        min_weight_index = w.index(min(w))
        max_profit = p[min_weight_index]
        min_weight = w[min_weight_index]
       
        if(min_weight <= cap):
            cap -= min_weight
            mw += max_profit
        else:
            mw += max_profit*cap/min_weight
            break
       
        p.remove(max_profit)
        w.remove(min_weight)


    return mw


# FUNCTION OF BALANCE OF BOTH
def balance_of_both(n,cap,p,a,w):
    bb = 0

    for i in range(n):
        if not p:  # check if the p list is empty
            break
        max_a_index = a.index(max(a))
        max_a = a[max_a_index]
        max_profit = p[max_a_index]
        max_weight = w[max_a_index]
        if(max_weight <= cap):
            cap -= max_weight
            bb += max_profit
        else:
            bb += max_profit*cap/max_weight
            break
        p.remove(max_profit)
        w.remove(max_weight)
        a.remove(max_a)

    return bb



if __name__ == "__main__":
    p = [] #Profit list
    w = [] #weight list
    a = [] #ratio list
    

# READ THE USER INPUT

    n,cap,p,w,a = element()
    
    p1 = p.copy()
    w1 = w.copy()
# CALL MAXIMUM PROFIT FUNCTION

    mp = largest_profit(n,cap,p,w)
    print(f"Maximum profit is : {mp}")

    
# CALL MINIMUM WEIGHT FUNCTION

    mw = minimum_weight(n,cap,p,w)
    print(f"Minimum weight is : {mw}")
   

# CALL BALANCE OF BOTH FUNCTION

    bb = balance_of_both(n,cap,p1,a,w1)
    print(f"Balance_of_both is : {bb}")

