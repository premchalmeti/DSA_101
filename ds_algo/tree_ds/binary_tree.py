#       tree
#       ----
#        1    <-- root
#      /   \
#     2     3
#    / \  
#   4   5


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()
    
    def preorder(self):
        print(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print(self.data)

    # height
    # level
    # find node
    # get node distance


if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    root.set_left(node2)
    root.set_right(node3)

    node2.set_left(node4)
    node2.set_right(node5)

    print("Pre order")
    root.preorder()

    print("Post order")
    root.postorder()

    print("In order")
    root.inorder()
