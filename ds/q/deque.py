from ds.q import CircularQueue, exceptions


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
    dq = Deque(4)

    dq.enq('Song1')
    dq.enq_front('Song2')
    dq.enq_front('Song3')

    # song3
    print(dq.deq())
    # song1
    print(dq.deq_rear())

    dq.enq_front('Song4')

    # song4
    print(dq.deq())

    # song2
    print(dq.deq())
