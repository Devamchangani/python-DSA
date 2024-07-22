s = "ddddddddd"
co = 0
longs = ""
if len(s) == 1:
    return 1
for i in range(len(s)):
    # print(i)
    for j in range(i, len(s)):
        # print(j)
        if s[j] not in longs:
            longs += s[j]
            # print(longs)
        else:
            # print(longs)
            if co <= len(longs):
                co = len(longs)
            longs = ""
            break
    # print(longs)
print(co)