#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    sortArr = sorted(candles)
    maxNum = max(sortArr)
    totalNum = 0
    for i in range(0, len(candles)):
        if sortArr[i] == maxNum:
            totalNum += 1

    return totalNum

birthdayCakeCandles([3,2,1,3])
