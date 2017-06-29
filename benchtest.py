#!/usr/bin/env python3

import random as r
import time
from pysort import *
from quicksort import *
from mergesort import *

def testing(fun):
    t0 = time.time()
    for i in range(10):
        li = []
        for i in range(10000):
            li.append(r.randint(-10000, 10000))
        fun.sort(li)
    print(str(fun) + ": %.2f sec" % (time.time() - t0))

def main():
    testing(PySort())
    testing(QuickSort())
    testing(MergeSort())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
