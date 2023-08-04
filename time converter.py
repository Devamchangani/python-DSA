#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_components = s.split(":")
    hours = int(time_components[0])
    minutes = int(time_components[1])
    seconds = int(time_components[2][:2])  # Remove 'AM' or 'PM' from seconds if present
    am_pm = time_components[2][-2:]

    # Handle special cases for 12:00 AM and 12:00 PM
    if hours == 12:
        hours = 0 if am_pm == 'AM' else 12
    else:
        hours += 12 if am_pm == 'PM' else 0

    # Return the result in 24-hour format
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
