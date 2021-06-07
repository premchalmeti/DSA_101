from binary_tree import Node


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def _create_node(self, data):
        return Node(data)

    def add_node(self, node):
        if not isinstance(node, Node):
            node = self._create_node(node)

        if not self.root:
            self.root = node
            return

        curr = self.root
        prev = None

        while curr:
            prev = curr
            if node.data > curr.data:
                curr = node.right
            elif node.data < curr.data:
                curr = node.left
            else:
                print("duplicate", node.data, "key")

        if not prev:
            self.root = node
        elif node.data < prev.data:
            print("Added", node.data, "to", prev.data, "left")
            prev.left = node
        else:
            print("Added", node.data, "to", prev.data, "right")
            prev.right = node

    def inorder_traverse(self):
        self.root.inorder()
    
    def preorder_traverse(self):
        self.root.preorder()
    
    def postorder_traverse(self):
        self.root.postorder()


if __name__ == '__main__':
    bst = BinarySearchTree()
    data = [67,34,80,12,45,78,95,10,38,60,78,95,86]

    for d in data:
        bst.add_node(d)

    bst.inorder_traverse()
