#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    total_gas = 0  # Total gas in the truck
    current_gas = 0  # Gas available at the current station
    start_index = 0

    for i in range(len(petrolpumps)):
        total_gas += petrolpumps[i][0] - petrolpumps[i][1]
        current_gas += petrolpumps[i][0] - petrolpumps[i][1]
    
        if current_gas < 0:
            current_gas = 0
            start_index = i + 1

    if total_gas >= 0:
        return start_index
    else:
        return -1

if __name__ == '__main__':

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(result)
