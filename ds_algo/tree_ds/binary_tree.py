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


# the following top view prints from current node to left and right
# def top_view(root, c_lvl, lvl_visits):
#     if not root:
#         return []

#     if c_lvl not in lvl_visits:
#         print(root.data, end=" ")
#         lvl_visits.append(c_lvl)
    
#     l_visits = top_view(root.left, c_lvl-1, lvl_visits)
#     lvl_visits.extend(l_visits)

#     r_visits = top_view(root.right, c_lvl+1, lvl_visits)
#     lvl_visits.extend(r_visits)

#     return lvl_visits

# use stack to print root and left subtree and q to print right subtree
def top_view(root):
    from collections import deque, OrderedDict

    q = deque()
    q.append({
        'node': root, 
        'level': 0
    })
    tree_map = OrderedDict()

    while len(q) > 0:
        entry = q.popleft()
        node = entry['node'] 
        level = entry['level']

        if level not in tree_map:
            tree_map[level] = node.data
            # print(level, node.data)

        if node.left:
            q.append({
                'node': node.left,
                'level': level - 1
            })

        if node.right:
            q.append({
                'node': node.right,
                'level': level + 1
            })

    print(tree_map)

    # for d in tree_map.values():
    #     print(d, end=" ")


if __name__ == '__main__':
    # root = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)

    # root.set_left(node2)
    # root.set_right(node3)

    # node2.set_left(node4)
    # node2.set_right(node5)

    # print("Pre order")
    # root.preorder()

    # print("Post order")
    # root.postorder()

    # testcase 1:
    #      1
    #       \
    #        2
    #         \
    #          5
    #         /  \
    #        3    6
    #         \
    #          4

    # root = Node(1)
    # node2 = Node(2)
    # node5 = Node(5)
    # node3 = Node(3)
    # node6 = Node(6)
    # node4 = Node(4)

    # root.set_right(node2)
    # node2.set_right(node5)
    # node5.set_left(node3)
    # node5.set_right(node6)
    # node3.set_right(node4)

    # top_view(root)

    # testcase 2
    # https://stackoverflow.com/questions/31385570/trying-to-print-top-view-of-a-tree-using-two-if-statements
    # https://i.stack.imgur.com/mowQ3.png

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node3.set_left(node5)
    node3.set_right(node2)

    node5.set_left(node1)
    node5.set_right(node4)

    node1.set_right(node9)

    node2.set_left(node6)
    node2.set_right(node7)

    node7.set_left(node8)

    print("Top view for Tree is")
    top_view(node3)
