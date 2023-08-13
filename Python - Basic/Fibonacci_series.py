def fibonacci():
    n = int(input("Enter a number: "))
    print(f"Fibonacci series upto {n} is: ")
    f = 1
    s = 1
    print(f)
    print(s)
    for i in range(n-2):
        l = f+s
        print(l)
        s = f
        f = l
    print(f)

if __name__ == "__main__":
    fibonacci()
