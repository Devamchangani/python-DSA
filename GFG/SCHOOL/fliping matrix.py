
def flippingMatrix(matrix):
    # Write your code here
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += max(max(matrix[i][j],matrix[2*n-i-1][j]),max(matrix[i][2*n-j-1],matrix[2*n-i-1][2*n-j-1]))
    return suma
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)
        print(result)
