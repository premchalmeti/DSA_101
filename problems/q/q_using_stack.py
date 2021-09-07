from DSA_101.ds.stacks import exceptions
from ds.stacks import Stack
from ds.q import exceptions


class Queue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enq(self, data):
        self.stack1.push(data)

    def deq(self) -> object:
        if not (self.stack1 and self.stack2):
            raise exceptions.QueueUnderFlowError()

        if not self.stack2:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    q = Queue()
    q.enq(2)
    q.enq(4)

    # 2
    print(q.deq())

    q.enq(5)
    q.enq(8)

    # 4
    print(q.deq())

    q.enq(4)

    # 5
    print(q.deq())
    # 8
    print(q.deq())
