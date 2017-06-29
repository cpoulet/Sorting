#!/usr/bin/env python3

import sys

class QuickSort:

    def __str__(self):
        return "QuickSort"

    def sort(self, li):
        if type(li) is not list:
            raise Exception('Argument passed is not a list')
        self._partition(li, 0, len(li) - 1)
        return li

    def _partition(self, li, start, end):
        if (end - start) <= 0:
            return 0
        p = li[end]
        i = start
        j = i
        while j < end:
            if li[j] < p:
                li[i], li[j] = li[j], li[i]
                i += 1
            j += 1
        li[i], li[j] = li[j], li[i]
        self._partition(li, start, i - 1)
        self._partition(li, i + 1, end)

def main(argv):
    if len(argv) != 2:
        raise Exception('usage: ' + argv[0] + ' list')
    ar = [int(i) for i in argv[1].strip().split()]
    print(QuickSort().sort(ar))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(str(e))
