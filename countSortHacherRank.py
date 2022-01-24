#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    max_value = max(arr);
    print(max_value)
    index_list = [0]*100
    print(index_list)
    for j in range(0,len(arr)):
        index_list[arr[j]] +=1
    return index_list

