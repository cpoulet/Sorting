#!/usr/bin/env python3

import sys

class PySort:

    def __str__(self):
        return "PySort"

    def sort(self, li):
        if type(li) is not list:
            raise Exception('Argument passed is not a list')
        return li.sort()

def main(argv):
    if len(argv) != 2:
        raise Exception('usage: ' + argv[0] + ' list')
    li = [int(i) for i in argv[1].strip().split()]
    print(PySort().sort(li))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(str(e))
