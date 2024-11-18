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
def plusMinus(arr):
    negative = [];
    positive = [];
    zeroPosition = [];
    for i in arr:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zeroPosition.append(i)
    print(len(positive)/len(arr))
    print(len(negative)/len(arr))
    print(len(zeroPosition)/len(arr))



plusMinus([-4, 3, -9, 0, 4, 1])
