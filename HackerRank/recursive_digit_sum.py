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
def superDigitHelper(num):
    if len(num) == 1:
        return int(num)
    
    sumOfDigits = sum(int(ch) for ch in num)
    return superDigitHelper(str(sumOfDigits))

def superDigit(n, k):
    # Write your code here
    val = 0
    for ch in n:
        val += int(ch)*k
        
    return superDigitHelper(str(val))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
