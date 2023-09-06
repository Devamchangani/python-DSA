l = []
l_1 = []
sen = []
send = []

l2 = []
l_2 = []
res2 = []
rec = []

n = int(input("Enter a Number size: "))


# -------------------------------------Sender-----------------------------
#sender

for i in range(n):
  s = int(input("Enter sender 0 or 1 only: "))
  l.append(s)


if n%3 == 0:
  size = 3
elif n%4 == 0:
  size = 4
elif n%5 == 0:
  size = 5
else:
  print("not allow a prime number")

#  saprate a list in 5 size

for i in range(0, len(l), size):
  l_1.append(l[i:i+size])


# addition of all list

for j in range(0, len(l_1[0])):
    tmp = 0
    for i in range(0, len(l_1)):
        tmp = tmp + l_1[i][j]
    sen.append(tmp)

# parity sender

for i in range(len(sen)):
  if(sen[i] %2 == 0):
    send.append(0)
  else:
    send.append(1)
print(f"sender bits: {send}")


# ----------------------------Reciver-------------------------------------

#reciver
for i in range(n):
  r = int(input("Enter reciver 0 or 1 only: "))
  l2.append(r)


#  saprate a list in 5 size

for i in range(0, len(l2), size):
  l_2.append(l2[i:i+size])


# addition of all list

for j in range(0, len(l_2[0])):
    tmp = 0
    for i in range(0, len(l_2)):
        tmp = tmp + l_2[i][j]
    res2.append(tmp)

# parity reciver
rec = []
for i in range(len(res2)):
  if(res2[i] %2 == 0):
    rec.append(0)
  else:
    rec.append(1)
print(f"reciver bits: {rec}")


# ---------------------------Compare both parity bits---------------------

if(send == rec):
  print("hello")
else:
  print("byy")

