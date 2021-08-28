import os, sys;
sys.path.append(os.environ.get('DSPATH', ''));

import utils


class QueueOverFlowError(OverflowError):
    pass

class QueueUnderFlowError(Exception):
    pass


class CQueue:
    def __init__(self, _max: int=None):
        self.__container = []

        self.front = 0
        self.rear = -1

        self.max = _max

    def enq(self, item: object):
        if self.rear == self.max:
            raise QueueOverFlowError(self.max)
        self.rear += 1
        self.__container.insert(self.rear, item)

    def deq(self) -> object:
        if not self:
            raise QueueUnderFlowError()

        item = self.__container[self.front]
        self.__container[self.front] = None
        self.front += 1
        return item

    @utils.deprecated('is_empty() is deprecated. Use bool(q) instead')
    def is_empty(self):
        return self._is_empty()

    def _is_empty(self):
        return self.front == self.rear + 1

    def __bool__(self):
        return not self._is_empty()

    def __len__(self):
        return len(self.__container)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}{self.__container}>"
    
    __repr__ = __str__


if __name__ == '__main__':
    playlist = CQueue()

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
