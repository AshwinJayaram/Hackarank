#!/bin/python3

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

'''
Given a square matrix, calculate the absolute difference between
the sums of its diagonals.

For example, the square matrix arr  is shown below:


'''

def diagonalDifference(arr):
    rdiag=arr[0][0]
    ldiag=0
    for i in range(1,len(arr)):
        rdiag=rdiag+arr[i][(i+1)-1]
    for i in range(len(arr)):
        ldiag=ldiag+arr[i][(len(arr)-1)-i]
    if ldiag>rdiag:
        diff=ldiag-rdiag
    else:
        diff=rdiag-ldiag
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
