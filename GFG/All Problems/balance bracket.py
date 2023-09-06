#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    no_match = False
    
    for b in s:
        if b in brackets.keys():
            stack.append(b)
        else:
            if stack:
                a = stack.pop()
            else:
                no_match = True
                break
            if b != brackets[a]:
                no_match = True
                break
    return 'NO' if (no_match or stack) else 'YES'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)