
while(True):
    print("Press q to quit")
    a = input("Enter a number : ")
    
    if a == "q":
        break

    try:
        a = int(a)
        if a>6:
            print("You enterd a number greater then 6")
    except Exception as e:
        print("please not enter a string")
print("Thanks for playing this game")