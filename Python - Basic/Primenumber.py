def prime():
    n = int(input("Enter a Number: "))
    print(f"Under {n}  prime number is:")
    m = 2
    while(m <= n):
        i = 2
        flag = 0
        while(i <= m/2):
            if(m % i == 0):
                flag = 1
                break
            i = i + 1
        if(flag == 0):
            print(m)

        m = m +1


if __name__ == "__main__":
    prime()