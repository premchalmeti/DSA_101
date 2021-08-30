import os, sys;
sys.path.append(os.environ.get('DSPATH', ''));

import utils
from cqueue.exceptions import QueueOverFlowError, QueueUnderFlowError

class Queue:
    def __init__(self, _max: int=None):
        self._container = []

        self.front = self.rear = -1

        self.max = _max

    def enq(self, item: object):
        if self.max and self.rear == self.max-1:
            raise QueueOverFlowError(self.max)
        self.rear += 1
        if self.front == -1:
            self.front += 1
        self._container.insert(self.rear, item)

    def deq(self) -> object:
        if not self:
            raise QueueUnderFlowError()

        item = self._container[self.front]
        self._container[self.front] = None
        self.front += 1
        return item

    @utils.deprecated('is_empty() is deprecated. Use bool(q) instead')
    def is_empty(self):
        return self._is_empty()

    def _is_empty(self):
        return (self.front==self.rear==-1) or (self.front == self.rear+1)

    def __bool__(self):
        return not self._is_empty()

    def __len__(self):
        return len(self._container)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}{self._container}>"
    
    __repr__ = __str__


if __name__ == '__main__':
    playlist = Queue()

    playlist.enq("Song 1")
    playlist.enq("Song 2")

    print(playlist.deq())
    print(playlist.deq())

    playlist.enq("Song 3")
    playlist.enq("Song 4")
    playlist.enq("Song 5")

    print(playlist.deq())
    print(playlist.deq())
    print(playlist.deq())
