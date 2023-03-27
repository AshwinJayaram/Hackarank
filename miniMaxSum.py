#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''Given five positive integers, find the minimum
and maximum values that can be calculated by summing exactly
four of the five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.
'''

def miniMaxSum(arr):
    l=[]
    
    for i in range(len(arr)):
        sum=0
        for j in range(len(arr)):
            if i!=j:
                sum+=arr[j]
            else:
                continue
        l.append(sum) 
    minimum=min(l)
    maximum=max(l)
    print(minimum,maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
