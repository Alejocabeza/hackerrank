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
def miniMaxSum(arr):
    arrMin = [];
    arrMax = [];
    sortArr = sorted(arr)
    for i in range(0, len(arr)-1):
        arrMin.append(sortArr[i])
        arrMax.append(sortArr[i+1])
    print(sum(arrMin), sum(arrMax))

miniMaxSum([7,69,2,221,8974])
