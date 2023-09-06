def main():
    print("hello")

def size():
    l = []
    n = int(input("Enter a Number size: "))
    for i in range(n): 
        s = int(input("Enter sender 0 or 1 only: "))
        l.append(s)
    # return l
    print(l)

if __name__ == "__main__":
    main()
    size()