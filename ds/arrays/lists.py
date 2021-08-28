# basic operations
# traverse
# insert
# delete
# search
# update
from __future__ import print_function
import sys


def _traverse(sarr=None, iarr=None):
    # traverse: to only print
    # list comprehension to generate new list by traversing list
    sarr = sarr or list()
    iarr = iarr or list()

    for no in iarr:
        sys.stdout.write(str(no))

    sys.stdout.flush()

    print(', '.join(sarr))

    # slicing
    print(sarr[::])



def _insert(arr, index, ele):
    # insertion
    arr.insert(index, ele)
    # arr.append(ele)
    # arr.extend([ele])


def _update(arr, ele, index=None, oele=None):
    index = index or arr.index(oele)

    arr[index] = ele


def _delete(arr, start=None, end=None, ele=None):
    if start and end:
        del arr[start:end]
    elif start:
        del arr[start]
        # arr.pop(start)
    elif ele:
        # if ele not in list throws ValueError
        arr.remove(ele)
    else:
        arr.pop()
    # clear() to delete all eles


def _search(arr, ele):
    # if ele not in arr throws ValueError
    # todo: implement binary search on strings
    # count(ele)-> returns count of ele
    # print(arr.index(ele))
    # membership test
    print(ele in arr)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    names = ['premkumar', 'kartik', 'milind']

    _traverse(iarr=numbers)
    _traverse(sarr=names)

    _insert(names, index=1, ele='shubham')
    _traverse(sarr=names)

    _update(names, index=1, ele='suvarna')
    _update(names, oele='suvarna', ele='prem')
    _traverse(sarr=names)

    _delete(names, ele='shubham')
    # _delete(names, start=1)
    print(names)

    _search(names, 'premkumar')
