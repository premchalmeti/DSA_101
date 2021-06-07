
def preorder_traverse(node):
    if not node:
        return
    print(node.data, end=" ")
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def inorder_traverse(node):
    if not node:
        return
    inorder_traverse(node.left)
    print(node.data, end=" ")
    inorder_traverse(node.right)


def postorder_traverse(node):
    if not node:
        return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end=" ")


if __name__ == '__main__':
    from linked_list_representation import Node

    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')
    nodeH = Node('H')
    nodeI = Node('I')
    nodeJ = Node('J')

    nodeA.set_left(nodeB)
    nodeA.set_right(nodeC)

    nodeB.set_left(nodeD)
    nodeB.set_right(nodeE)

    nodeE.set_left(nodeH)
    nodeE.set_right(nodeI)

    nodeC.set_left(nodeF)
    nodeC.set_right(nodeG)

    nodeG.set_left(nodeJ)

    print("\nPre order traversal:\n")
    preorder_traverse(nodeA)

    print("\nIn order traversal:\n")
    inorder_traverse(nodeA)

    print("\nPost order traversal:\n")
    postorder_traverse(nodeA)
