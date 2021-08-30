import os, sys;
sys.path.append(os.environ.get('DSPATH', ''));

from cqueue import Queue, exceptions


class CircularQueue(Queue):
    def __init__(self, max_: int):
        super().__init__(max_)
        self._container = [None]*max_

    def enq(self, e: object):
        if self._is_full(): raise exceptions.QueueOverFlowError()
        self.rear = (self.rear+1) % self.max
        self._container[self.rear] = e

        if self.front == -1:
            self.front += 1

    def deq(self):
        if not self:    raise exceptions.QueueUnderFlowError()
        item = self._container[self.front]
        self._container[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1) % self.max
        return item

    def _is_full(self):
        return self.front == self.rear+1 \
            or self.front==0 and self.rear==self.max-1

    def _is_empty(self):
        return self.front == -1


if __name__ == '__main__':
    cq = CircularQueue(4)

    for i in range(3):
        cq.enq(i)

    for _ in range(3):
        print(cq.deq())
