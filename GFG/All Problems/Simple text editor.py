Q = int(input())
S = ''
prevOp = []
for _ in range(Q):
    ops = input()
    if ops[0] == '1':
        prevOp.append(S)
        S += ops[2:]
    if ops[0] == '2':
        prevOp.append(S)
        ind = int(ops[2:])
        S = S[:len(S)-ind]
    if ops[0] == '3':
        ind = int(ops[2:])
        print(S[ind-1])
    if ops[0] == '4':
        S = prevOp.pop()