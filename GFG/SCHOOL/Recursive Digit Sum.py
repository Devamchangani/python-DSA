#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    def recursive_super_digit(number):
        if len(number) == 1:
            return int(number)
        digit_sum = sum(int(digit) for digit in number)
        return recursive_super_digit(str(digit_sum))
    
    initial_sum = sum(int(digit) for digit in n) * k
    return recursive_super_digit(str(initial_sum))

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
