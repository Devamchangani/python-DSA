#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in grid:
        for i in range(len(grid)):
            grid[i] = sorted(grid[i])
        
        # Check if columns are in ascending order
        for col in range(len(grid[0])):
            for row in range(1, len(grid)):
                if grid[row][col] < grid[row - 1][col]:
                    return "NO"
        
        return "YES"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
