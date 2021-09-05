from __future__ import annotations
from dataclasses import dataclass, field
from ds.linked_list import exceptions


@dataclass
class Node:
    data: object
    link: Node = field(default=None, init=False)

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}({self.data})>'
    
    __repr__ = __str__


NODE_CLASS = Node


def change_node_cls(cls):
    global NODE_CLASS
    NODE_CLASS = cls


def get_node_cls():
    return NODE_CLASS


class SinglyList:
    def __init__(self, data=None):
        self.head = self._create_node(data) if data else None
        self.rear = self.head

    def _create_node(self, data) -> Node:
        return NODE_CLASS(data)

    def _check_input(self, data, node: Node):
        if not data and not node:
            raise ValueError("Data or Node is needed for New Node")
        if data and node:
            raise ValueError("Data and Node are mutually exclusive")

    def append_data(self, data):
        node = self._create_node(data)
        self.append_node(node)

    def append_node(self, node: Node):
        # inserting first node
        if self.head is None:
            self.head = node
        else:
            self.rear.link = node

        self.rear = node

    def prepend_data(self, data):
        node = self._create_node(data)
        self.prepend_node(node)

    def prepend_node(self, node: Node):
        node.link = self.head
        self.head = node

    def delete_node(self, node):
        self.delete_data(node.data)

    def delete_data(self, data):
        temp_node = self.head
        prev = None

        while temp_node:
            if temp_node.data == data:
                break

            prev = temp_node
            temp_node = temp_node.link

        if not temp_node:
            raise exceptions.NodeNotFoundError(f"{data} node not found")

        # move head if is first node
        if self.head == temp_node:
            self.head = self.head.link
        else:
            prev.link = temp_node.link

        # move rear back if deleting end node
        if temp_node == self.rear:
            self.rear = prev

        del temp_node

    def reverse(self):
        current = self.head
        prev = None
        next = None

        while current:
            next = current.link

            current.link = prev

            prev = current
            current = next

        self.head = prev

    def print_mid(self):
        current = self.head
        end = self.head

        while end is not None and end.link is not None:
            current = current.link

            end = end.link.link

        print(current.data, 'is mid')

    def __str__(self):
        if not self.head:
            return "LinkedList is Empty"

        s = []
        tmp_node = self.head
        s.append('HEAD')

        while tmp_node:
            s.append(str(tmp_node))
            tmp_node = tmp_node.link

        s.append('END')
        return " >> ".join(s)

    __repr__ = __str__


if __name__ == '__main__':
    playlist = SinglyList("Song1")
    playlist.append_data("Song2")
    playlist.prepend_data("Song0")
    playlist.append_data("Song3")

    # Song0 -> Song1 -> Song2 -> Song3
    print(playlist)

    # delete between
    playlist.delete_data("Song2")
    # Song0 -> Song1 -> Song3
    print(playlist)

    # delete head
    playlist.delete_data("Song0")
    # Song1 -> Song3
    print(playlist)

    # delete end
    playlist.append_data('Song4')
    playlist.delete_data('Song4')
    # Song1 -> Song3
    print(playlist)
