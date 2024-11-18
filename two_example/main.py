#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n+1):
        sys.stdout.write(' ' * (n-i) + '#' * i)
        sys.stdout.write('\n')

staircase(6)
