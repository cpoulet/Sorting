#!/usr/bin/env python3

import random as r
import time
import multiprocessing
from pysort import *
from quicksort import *
from mergesort import *
from insertsort import *
from bubblesort import *

def fast_testing(fun):
    t0 = time.time()
    for i in range(10):
        li = []
        for i in range(1000):
            li.append(r.randint(-10000, 10000))
        fun.sort(li)
    print("%-12s" % str(fun) + ": %.2f sec" % (time.time() - t0))

def medium_testing(fun):
    t0 = time.time()
    for i in range(10):
        li = []
        for i in range(2000):
            li.append(r.randint(-10000, 10000))
        fun.sort(li)
    print("%-12s" % str(fun) + ": %.2f sec" % (time.time() - t0))

def long_testing(fun):
    t0 = time.time()
    for i in range(10):
        li = []
        for i in range(10000):
            li.append(r.randint(-10000, 10000))
        fun.sort(li)
    print("%-12s" % str(fun) + ": %.2f sec" % (time.time() - t0))

def main():
    sortingalgo = [PySort, QuickSort, MergeSort, InsertSort, BubbleSort]
    print('\n_________________FAST_TESTS_____________________')
    for algo in sortingalgo:
        fast_testing(algo())
    print('\n________________MEDIUM_TESTS_____________________')
    for algo in sortingalgo:
        p = multiprocessing.Process(target=medium_testing, args=(algo(),))
        p.start()
        p.join(5)
        if p.is_alive():
            print ("%-12s" % str(algo()) + ': Sorting is longer than 5 sec...Process killed')
            p.terminate()
            p.join()
    print('\n_________________LONG_TESTS_____________________')
    for algo in sortingalgo:
        p = multiprocessing.Process(target=long_testing, args=(algo(),))
        p.start()
        p.join(5)
        if p.is_alive():
            print ("%-12s" % str(algo()) + ': Sorting is longer than 5 sec...Process killed')
            p.terminate()
            p.join()

if __name__ == "__main__":
    main()
#    try:
#        main()
#    except Exception as e:
#        print(str(e))
