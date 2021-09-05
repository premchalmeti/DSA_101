from ds.trees import exceptions
from ds.stacks import Stack

tree_stack = Stack()


class Node:
    def __init__(self, data):
        self.__data = data
        self.childs = []

    def append_child(self, n):
        if not isinstance(n, Node):
            n = Node(n)

        self.childs.append(n)

    def get_data(self):
        return self.__data

    def get_child(self, d):
        if isinstance(d, Node):
            d = d.get_data()
        return next(filter(lambda c:c.get_data() == d, self.childs), None)

    def __eq__(self, o: object) -> bool:
        return self.get_data() == o.get_data()

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.get_data()}>'

    __repr__ = __str__


class Tree:
    def __init__(self, n=None):
        self.set_root(n)

    def append(self, node, parent):
        if not self.get_root():
            raise exceptions.EmptyTreeException("Tree is not created yet")

        if isinstance(parent, Node):
            parent = parent.get_data()

        root = self.get_root()

        tree_stack.push(root)
        curr = root

        while not tree_stack.is_empty():
            curr = tree_stack.pop()

            if curr.get_data() == parent:
                break

            for c in curr.childs:
                tree_stack.push(c)

        if not curr.get_data() == parent:
            raise exceptions.ParentNodeNotFound(f"{parent} parent node not found")

        if curr.get_child(node):
            raise exceptions.ChildAlreadyExists(f"{node} child already exists")

        curr.append_child(node)
        print("Added", curr, "->", node)

    def set_root(self, root):
        if not isinstance(root, Node):
            root = Node(root)

        self.__root = root

    def get_root(self):
        return self.__root

    def traverse(self):
        # level order traversal
        tree_stack.clear()

        from collections import deque

        q = deque()

        q.append(self.get_root())

        while len(q) > 0:
            n = q.popleft()

            print(n.get_data(), end=" ")

            for c in n.childs:
                q.append(c)
        
        print()


if __name__ == '__main__':
    clish_tree = Tree("admin")

    clish_tree.append("show", parent="admin")
    clish_tree.append("user", parent="admin")

    clish_tree.append("add", parent="user")
    clish_tree.append("modify", parent="user")
    clish_tree.append("delete", parent="user")

    clish_tree.traverse()
