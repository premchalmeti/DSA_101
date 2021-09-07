from dataclasses import dataclass
from ds.linked_list.singly import Node, SinglyList
from ds.linked_list import exceptions


@dataclass
class PriorityNode(Node):
    priority: int

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(data={self.data}, priority={self.priority})'
    __repr__ = __str__

class PriorityLinkedList(SinglyList):
    NODE_CLS = PriorityNode

    def __init__(self, data=None, priority=None):
        self.head = self._create_node(data, priority) if data and priority else None

class PriorityQueue:
    def __init__(self):
        self.list = PriorityLinkedList()

    def enq(self, data, priority):
        tmp_node = self.list.head
        prev = None

        # lower no indicates higher priority
        while tmp_node and tmp_node.priority <= priority:
            prev = tmp_node
            tmp_node = tmp_node.link

        nn = self.list._create_node(data, priority)
        nn.link = tmp_node

        if prev:
            prev.link = nn
        else:
            self.list.head = nn

    def deq(self):
        if not self.list.head:
            raise exceptions.LinkedListEmptyError()
        tmp_node = self.list.head
        self.list.head = self.list.head.link
        return tmp_node

    def __str__(self) -> str:
        return str(self.list)
    
    __repr__ = __str__


if __name__ == '__main__':
    pq = PriorityQueue()

    pq.enq('lowest', priority=3)
    pq.enq('highest', priority=1)
    pq.enq('mid', priority=2)

    print(pq)

    # highest
    print(pq.deq())

    # mid
    print(pq.deq())

    # lowest
    print(pq.deq())

    # expect LinkedListEmptyError
    print(pq.deq())
