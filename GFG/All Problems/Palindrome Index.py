#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if is_palindrome(s):
        return -1

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            elif is_palindrome(s[:n-i-1] + s[n-i:]):
                return n - i - 1

    return -1
    
    
def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
