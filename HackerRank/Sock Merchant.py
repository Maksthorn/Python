#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, bag_of_socks):
    unique=set()
    pair=list()

    for sock in sorted(bag_of_socks):   
      if sock in unique:
          unique.remove(sock)
          pair.append(sock)
      else:
          unique.add(sock)
       
    return len(pair)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
