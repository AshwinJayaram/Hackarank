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
'''
Converts time from 12hr format to military(24hr)clock format

'''
def timeConversion(s):
    new_s=" "
    sp=s.split(':')
    tm=sp[2][2:4]
    sp[2]=sp[2][0:2]
    if int(sp[0])>12 or int(sp[1])>=60 or int(sp[2])>=60:
        print("Error")
        sys.exit()
    if tm.upper()=='AM':
        if sp[0]=='12':
            
            new_s="0"+str((int(sp[0])-12))+":"+str(sp[1])+":"+str(sp[2])
        else:
            new_s=str((sp[0]))+":"+str(sp[1])+":"+str(sp[2])
            
    else:
        if sp[0]=='12':
            new_s=str(sp[0])+":"+str(sp[1])+":"+str(sp[2])
        else:
            new_s=str(int(sp[0])+12)+":"+str(sp[1])+":"+str(sp[2])
    return new_s





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
