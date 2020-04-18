
class Node(object):

    def __init__(self, data=0):
        super().__init__()
        self.next = None
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

