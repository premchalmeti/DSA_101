from __future__ import annotations
from typing import Optional

from ds.trees.exceptions import EmptyTreeException
from ds.q import Queue


class Node:
    def __init__(self, data: object):
        self.data = data

        self.left = None
        self.right = None

    def link_left(self, data: object):
        self.left = Node.create_node(data)

    def link_right(self, data: object):
        self.right = Node.create_node(data)

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data, end=" ")

        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.data, end=" ")

    @classmethod
    def create_node(cls, data: object) -> Node:
        return cls(data)

    def height(self) -> int:
        if not self.left and not self.right:
            return 1

        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()

        height = left_height if left_height > right_height else right_height

        return height + 1 

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}({self.data})>'
    
    __repr__ = __str__


class BinaryTree:
    def __init__(self, data: object=None, root: Node=None):
        if data and root:
            raise ValueError("data and root variable are mutually exclusive")
        elif data:
            root = Node(data)

        self.__root = root
        self.curr = root

    def find_node(self, node_obj: Node, data: object) -> Optional[Node]:
        if not node_obj:
            return None
        if node_obj.data == data:
            return node_obj
        return self.find_node(node_obj.left, data) \
            or self.find_node(node_obj.right, data)

    def _check_is_tree_empty(self):
        if not self.__root:
            raise EmptyTreeException("Tree is Empty")

    def link_left(self, new_data: object):
        self._check_is_tree_empty()
        self.curr.link_left(new_data)

    def link_right(self, new_data: object):
        self._check_is_tree_empty()
        self.curr.link_right(new_data)

    def goto(self, node_data: object, from_node: Node=None):
        node = self.find_node(from_node or self.curr, node_data)

        if not node:
            print(node_data, 'not found')
            exit(0)

        self.curr = node

    def get_root(self) -> Node:
        return self.__root

    def inorder(self):
        self.__root.inorder()
        print()
    
    def preorder(self):
        self.__root.preorder()
        print()

    def postorder(self):
        self.__root.postorder()
        print()

    def level_order(self):
        q = Queue()
        node = self.__root
        q.enq(node)

        while q:
            node = q.deq()

            if node:
                print(node.data, end=' ')

                q.enq(node.left)
                q.enq(node.right)
        
        print()

    @property
    def height(self):
        return self.__root.height()


if __name__ == '__main__':
    tree = BinaryTree('A')

    tree.link_left('B')
    tree.link_right('C')

    tree.goto('B')

    tree.link_left('D')
    tree.link_right('E')

    tree.goto('E')

    tree.link_left('H')
    tree.link_right('I')

    tree.goto('C', from_node=tree.get_root())
    tree.link_left('F')
    tree.link_right('G')

    tree.goto('G')
    tree.link_left('J')

    print("\nIn-order Traversal:")
    tree.inorder()

    print("\nPre-order Traversal:")
    tree.preorder()

    print("\nPost-order Traversal:")
    tree.postorder()

    print("\nLevel-order Traversal:")
    tree.level_order()

    print("\nHeight:", tree.height)

    #     1
    #    / \
    #   2   3
    #         \
    #          4
    #           \
    #            5

    tree = BinaryTree(1)

    tree.link_left(2)
    tree.link_right(3)
    tree.goto(3)
    tree.link_right(4)
    tree.goto(4)
    tree.link_right(5)

    print('\nHeight:', tree.height)
