#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#



'''
Rounds the grades of students to the nearest 5
applicable only to those who pass and when the diffrence is less
than 3 
'''
def gradingStudents(grades):
    result=[]
    for i in grades:
        if i>100 or i<0:
            sys.exit()
        if i<38:
            result.append(i)
            continue
        if i%5==0:
            result.append(i)
            continue
        
        temp=i
        flag=False
        for j in range(1,3):
            if (j+temp)%5==0:
                result.append(j+temp)
                flag=True
                break
            
        if flag==False:
                result.append(i)
                
        
    return result        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
