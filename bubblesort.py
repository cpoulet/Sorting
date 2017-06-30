#!/usr/bin/env python3

import sys

class BubbleSort:

    def __str__(self):
        return "BubbleSort"

    def sort(self, li):
        if type(li) is not list:
            raise Exception('Argument passed is not a list')
        return self._bubble(li)

    def _bubble(self, li):
        issorted = False
        while not issorted:
            issorted = True
            for i in range(len(li) - 1):
                if li[i] > li[i + 1]:
                    li[i], li[i + 1] = li[i + 1], li[i]
                    issorted = False
        return li

def main(argv):
    if len(argv) != 2:
        raise Exception('usage: ' + argv[0] + ' list')
    li = [int(i) for i in argv[1].strip().split()]
    print(BubbleSort().sort(li))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(str(e))
