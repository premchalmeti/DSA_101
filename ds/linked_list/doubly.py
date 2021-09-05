from dataclasses import dataclass
from singly import Node


class DNode(Node):
    prev: Node
    data: object
    nxt: Node


# to be implemented
class SinglyList:
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def _create_node(self, data):
        return DNode(data)

    def _check_data_or_node(self, data, node):
        if not data and not node:
            raise ValueError("Data or Node is needed for New Node")
        if data and node:
            raise ValueError("Data and Node are mutually exclusive")

    def prepend(self, data=None, node=None):
        self._check_data_or_node(data, node)

        if not node:
            node = self._create_node(data)

        node.next = self.head
        self.head = node

    def print_list(self):
        tmp_node = self.head
        print('HEAD >>', end=' ')

        while tmp_node:
            print(tmp_node.data, ">>", end=' ')
            tmp_node = tmp_node.next

        print('END', end=' ')
