import math

def input_val():
    global cap1, cap2, fill, vis
    vis = [[False for _ in range(100)] for _ in range(100)]
    cap1 = int(input("Enter capacity of jug 1: "))
    cap2 = int(input("Enter capacity of jug 2: "))
    fill = int(input("Enter Fillup liter: "))

    # return cap1, cap2, fill


def wjp(j1,j2):

    if (j1 == fill and j2 == 0) or (j2 == fill and j1 == 0):
        print(f"{j1}       {j2}")
        return True
    
    if not vis[j1][j2]:
        print(f"{j1}       {j2}")
        vis[j1][j2] = True
        return(wjp(0,j2) or wjp(j1,0) or wjp(j1,cap2) or wjp(cap1,j2) or wjp(j1 + min(j2,(cap1 - j1)),j2 - min(j2, (cap1 - j1))) or wjp(j1 - min(j1, cap2 - j2), j2 + min(j1,cap2 - j2)))

    return False

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a
    

if __name__ == "__main__":
    input_val()
    if fill % gcd(cap1,cap2) == 0:
        print(f"Solution is available!! \nFollow The Path: ")
        wjp(0,0)
    else:
        print(f"No solution is available for given values of jug1: {cap1} jug2: {cap2}")


# 2 ways
# from collections import defaultdict

# def waterjug(amt1,amt2,jg1,jg2,aim,visited):
#     if(amt1==aim and amt1==0) or(amt1==0 and amt2==aim):
#         print(amt1,amt2)
#         return True
#     if(visited[(amt1,amt2)]==False):
#         print(amt1,amt2)

#         visited[(amt1,amt2)]=True
#         return (waterjug(0,amt2,jg1,jg2,aim,visited) or waterjug(amt1,0,jg1,jg2,aim,visited) or waterjug(jg1,amt2,jg1,jg2,aim,visited) or waterjug(amt1,jg2,jg1,jg2,aim,visited) or waterjug(amt1+min(amt2,(jg1-amt1)),amt2-min(amt2,(jg1-amt1)),jg1,jg2 ,aim,visited) or waterjug(amt1-min(amt1,(jg2-amt2)),amt2+min(amt1,(jg2-amt2)),jg1,jg2,aim,visited))
#     else:
#         return False

# def solve(jg1,jg2,aim):
#     visited = defaultdict(lambda:False)
#     waterjug(0,0,jg1,jg2,aim,visited)

# jg1=int(input("Enter value of jug1:"))
# jg2=int(input("Enter value of jug2:"))
# aim=int(input("Enter value of aim:"))
# solve(jg1,jg2,aim)
