# lists are not efficient for queue implementation
# While appends and pops from the end of list are fast, 
# doing inserts or pops from the beginning of a list is slow 
# (because all of the other elements have to be shifted by one).
# refer: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

# to be implemented
def test_builtin_deque():
    from collections import deque
    dq = deque()

    dq.append('Song1')
    dq.appendleft('Song2')
    dq.appendleft('Song3')

    # song1
    print(dq.pop())
    # song3
    print(dq.popleft())

    dq.appendleft('Song4')

    # song4
    print(dq.popleft())

    # song2
    print(dq.pop())


import os, sys;
sys.path.append(os.environ.get('DSPATH', ''));

from cqueue import CircularQueue, exceptions


class Deque(CircularQueue):
    def enq_front(self, e: object):
        if self._is_full(): raise exceptions.QueueOverFlowError()

        if self.front == self.rear == -1:
            self.front = self.rear = 0
        else:
            self.front = (self.front-1+self.max) % self.max

        self._container[self.front] = e

    def deq_rear(self):
        if not self:    raise exceptions.QueueUnderFlowError()

        item = self._container[self.rear]
        self._container[self.rear] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear-1 + self.max) % self.max
        
        return item


if __name__ == '__main__':
    import pdb;pdb.set_trace()
    dq = Deque(4)

    dq.enq('Song1')
    dq.enq_front('Song2')
    dq.enq_front('Song3')

    # song1
    print(dq.deq())
    # song3
    print(dq.deq_rear())

    dq.enq_front('Song4')

    # song4
    print(dq.deq_front())

    # song2
    print(dq.deq())
