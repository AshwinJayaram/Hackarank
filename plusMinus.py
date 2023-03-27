#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
def plusMinus(arr):
    posval=0
    negval=0
    zerocount=0
    for i in arr:
        if i>0:
            posval+=1
        elif i<0:
            negval+=1
        else:
            zerocount+=1
    print(round(posval/len(arr),6))
    print(round(negval/len(arr),6))
    print(round(zerocount/len(arr),6))
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
