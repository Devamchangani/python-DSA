
def calculate_position(K):
    position = 0

    for i in range(1, K+1):
        
        if i % 2 == 0:
            position -= 1
        else:
            position += 3
    return position


T = int(input())


for i in range(T):
    K = int(input())
    position = calculate_position(K)
    print(position)


