#!/usr/bin/env python3

import sys

class MergeSort:

    def sort(self, li):
        if type(li) is not list:
            raise Exception('Argument passed is not a list')
        return self._devide(li)

    def _devide(self, li):
        l = len(li)
        if l <= 1:
            return li
        left = self._devide(li[:l//2])
        right = self._devide(li[l//2:])
        return self._conquer(left, right)

    def _conquer(self, left, right):
        li = []
        l, ll = 0, len(left)
        r, lr = 0, len(right)
        while l < ll and r < lr:
            if left[l] <= right[r]:
                li.append(left[l])
                l += 1
            else:
                li.append(right[r])
                r += 1
        while l < ll:
            li.append(left[l])
            l += 1
        while r < lr:
            li.append(right[r])
            r += 1
        return li

def main(argv):
    if len(argv) != 2:
        raise Exception('usage: ' + argv[0] + ' list')
    li = [int(i) for i in argv[1].strip().split()]
    print(MergeSort().sort(li))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(str(e))
