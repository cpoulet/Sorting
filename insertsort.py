#!/usr/bin/env python3

import sys

class InsertSort:

    def __str__(self):
        return "InsertSort"

    def sort(self, li):
        if type(li) is not list:
            raise Exception('Argument passed is not a list')
        for i in range(1, len(li)):
            if li[i] < li[i-1]:
                self._insert(li, li.pop(i))
        return li

    def _insert(self, li, val):
        for i in range(len(li)):
            if val < li[i]:
                li.insert(i, val)
                return

def main(argv):
    if len(argv) != 2:
        raise Exception('usage: ' + argv[0] + ' list')
    li = [int(i) for i in argv[1].strip().split()]
    print(InsertSort().sort(li))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(str(e))
