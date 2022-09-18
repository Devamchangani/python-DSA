T = int(input())

if T in range(26):
    for i in range(T):
        n = int(input())
        if n in range(2, 101):
            name = []
            score = []
            for j in range(n):
                l = input() .split()
                a = str(l[0])
                name.append(a)
                m = float(l[1])
                score.append(m)

            for j in range(n):
                if score[j] >= 0.00 and score[j] <= 100.00:
                    flag = 0
                else: 
                    flag = 1
                    break
            
            if flag == 0:
                s = []
                b = max(score)
                for i in range(len(score)):
                    if score[i] == b:
                        a = score.index(score[i])
                        s.append(name[i])
                s.sort(key=lambda x: x.lower())
                for i in range(len(s)):
                    print(s[i])