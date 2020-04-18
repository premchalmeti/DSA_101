
# lists are not efficient for this purpose as per python doc
# however, lists are not efficient for this purpose. While appends and pops
# from the end of list are fast, doing inserts or pops from the beginning of
# a list is slow (because all of the other elements have to be shifted by one).

# Q = list()
from collections import deque
Q = deque()


def _enqueue(ele):
    # Q.insert(0, ele)
    Q.append(ele)


def _deque():
    # return Q.pop()
    return Q.popleft()


if __name__ == '__main__':
    _enqueue('premkumar')
    _enqueue('kartik')

    print(_deque())
    print(_deque())
