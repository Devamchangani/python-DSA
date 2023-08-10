#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    dic = {}
    for i in range(len(words)):
        start = dic
        for j in range(len(words[i])):
            if words[i][j] not in start:
                start[words[i][j]] = {}
            start = start[words[i][j]]
            if '*' in list(start.keys()) or (j == len(words[i]) - 1 and (start)):
                print("BAD SET\n", words[i], sep = '')
                return
        start['*'] = True
    print('GOOD SET')


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
