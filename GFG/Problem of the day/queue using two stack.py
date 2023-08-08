q = int(input())
queue = []
for _ in range(q):
    ops = input().split()
    if ops[0] == '1': queue.insert(0,ops[1])
    elif ops[0] == '2': queue.pop()
    else: print(queue[-1])