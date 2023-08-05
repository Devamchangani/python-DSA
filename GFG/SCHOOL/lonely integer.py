#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    dict = Counter(a)
    n = False
    for num, count in dict.items():
        if count == 2:
            # print(num)
            continue
        else:
            n = True
            m = num

    
    if n == True:
        return m
    else:
        return -1

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
