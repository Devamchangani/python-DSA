a = 5 # Global variable
def fun1():
    global a
    print(a)
    a = 8 # Local variable
    print(a)

fun1()
print(a)