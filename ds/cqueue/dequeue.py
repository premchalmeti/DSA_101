# lists are not efficient for queue implementation
# While appends and pops from the end of list are fast, 
# doing inserts or pops from the beginning of a list is slow 
# (because all of the other elements have to be shifted by one).
# refer: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

# to be implemented

from collections import deque
Q = deque()


def _enqueue(ele):
    Q.append(ele)


def _deque():
    return Q.popleft()


if __name__ == '__main__':
    _enqueue('premkumar')
    _enqueue('kartik')

    print(_deque())
    print(_deque())
