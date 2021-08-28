"""
    Singly Linked List Implementation with following methods,
    append([data=data], [node=node])
    prepend([data=data], [node=node])
    insert_at(pos, [data=data], [node=node])
    print_list()
    reverse()
"""


class Node:

    def __init__(self, data=0):
        super().__init__()
        self.next = None
        self.prev = None
        self.data = data

    def link(self, new_node):
        self.next.prev = new_node
        new_node.prev = self
        self.next = new_node

# to be implemented
class SinglyList:
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def _create_node(self, data):
        return Node(data)

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
