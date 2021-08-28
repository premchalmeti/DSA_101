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
        self.data = data
    
    def __str__(self) -> str:
        return f'<{self.__class__.__name__}({self.data})>'
    
    __repr__ = __str__


class SinglyList:
    def __init__(self) -> None:
        self.head = None

    def _create_node(self, data):
        return Node(data)

    def _check_input(self, data, node):
        if not data and not node:
            raise ValueError("Data or Node is needed for New Node")
        if data and node:
            raise ValueError("Data and Node are mutually exclusive")

    def append(self, data=None, node=None):
        self._check_input(data, node)

        if not node:
            node = self._create_node(data)

        tmp_node = self.head

        while tmp_node:
            tmp_node = tmp_node.next

        tmp_node.next = node

    def prepend(self, data=None, node=None):
        self._check_input(data, node)

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

    def reverse(self):
        current = self.head
        prev = None
        next = None

        while current:
            next = current.next

            current.next = prev

            prev = current
            current = next

        self.head = prev

    def print_mid(self):
        current = self.head
        end = self.head

        while end is not None and end.next is not None:
            current = current.next

            end = end.next.next

        print(current.data, 'is mid')
