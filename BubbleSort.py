#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    counter = 0
    for i in range(0,len(a)) :
    
        for j in range(0,len(a)-1) :
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) :
                a[j+1],a[j] = a[j],a[j+1]
                counter+=1
            
    
    first = a[0]
    last = a[-1]
    print(f'Array is sorted in {counter} swaps.')
    print(f'First Element: {first}')
    print(f'Last Element: {last}')
    

#countSwaps([4,2,3,1])
