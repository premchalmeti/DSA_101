"""
    Note: duplicate keys are not allowed in BST
    1. searching node
    2. searching min and max node
    3. insertion
    4. deletion
"""
from ds.trees import BinaryTree, exceptions
from ds.trees.binary_tree import Node


class BinarySearchTree(BinaryTree):
    def insert(self, data, curr):
        if not curr:
            self.root = Node(data)
            return

        if data == curr.data:
            raise exceptions.DuplicateKeyError(f'{data} already exists in BST')
        elif data > curr.data:
            if not curr.right:
                curr.link_right(data)
                return
            else:
                self.insert(data, curr.right)
        elif data < curr.data:
            if not curr.left:
                curr.link_left(data)
                return
            else:
                self.insert(data, curr.left)

    def find_min(self, curr) -> object:
        if not curr.left:
            return curr.data
        return self.find_min(curr.left)

    def find_max(self, curr) -> object:
        if not curr.right:
            return curr.data
        return self.find_min(curr.right)

    def find(self, data, curr) -> bool:
        if not curr:
            return None
        elif data == curr.data:
            return curr
        elif data > curr.data:
            return self.find(data, curr.right)

        return self.find(data, curr.left)

    def _delete_case_a(self, parent, node):
        """
        CASE A: node has no childs
        """
        if parent == None:
            self.root = None
        elif parent.left == node:
            parent.left = None
        else:
            parent.right = None

        del node

    def _delete_case_b(self, parent, node):
        """
        CASE B: Node has exact 1 child
        """
        child = node.left or node.right
        if not parent:
            self.root = child
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child
        del node

    def _delete_case_c(self, parent, node):
        """
        CASE C: Node has 2 child nodes
        - Find the in-order successor of node by
            - Visiting the right child's leftmost child
        - Copy successor's data into node
        - Delete the successor by case A or case B
        """
        succ = node.right
        parent = node

        while succ.left:
            parent = succ
            succ = succ.left

        node.data = succ.data
        if succ.right:
            self._delete_case_b(parent, succ)
        else:
            self._delete_case_a(parent, succ)

    def delete(self, data):
        parent = self.root
        curr = parent

        while curr:
            if curr.data == data:
                break
            elif data > curr.data:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left

        if not curr:
            raise exceptions.NodeNotFound()
        elif curr.left and curr.right:
            self._delete_case_c(parent, curr)
        elif curr.left or curr.right:
            self._delete_case_b(parent, curr)
        else:
            self._delete_case_a(parent, curr)


if __name__ == '__main__':
    bst = BinarySearchTree()
    keys = [50, 30, 60, 38, 35, 55, 22, 59, 94, 13, 98]

    list(map(lambda k: bst.insert(k, bst.root), keys))
    print(bst.find_min(bst.root))
    print(bst.find_max(bst.root))
    print(not not bst.find(22, bst.root))
    print(not not bst.find(-1, bst.root))

    bst.delete(13)
    bst.delete(38)
    bst.delete(60)
