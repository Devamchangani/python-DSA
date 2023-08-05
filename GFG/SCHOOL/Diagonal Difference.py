import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range(l):
        # for j in range(i):
        j = i
        sum1 += arr[i][j]
        sum2 += arr[i][-(i+1)]

    return abs(sum1-sum2)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)