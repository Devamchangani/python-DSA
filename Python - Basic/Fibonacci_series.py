def fibonacci():
    n = int(input("Enter a number: "))
    print(f"Fibonacci series upto {n} is: ")
    a = 1
    b = 1
    l = [1]
    if n == 1:
        return l
    l.append(b)
    for i in range(n-2):
        c = a+b
        a = b
        b = c
        l.append(c)
    return l

if __name__ == "__main__":
    res = fibonacci()
    for i in res:
        print(i, end=" ")