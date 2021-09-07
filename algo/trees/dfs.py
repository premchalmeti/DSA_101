"""
DFS: Depth First Search

- DFS of Graph is done using Stack DS
- DFS of Tree is easier as trees are always connected and there are no cycles
- In-order, Pre-order, Post-order are DFS traversals for a Tree

"""

from ds.trees import BinaryTree


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.link_left(2)
    tree.link_right(3)

    tree.goto(3)
    tree.link_left(4)
    tree.link_right(5)

    print('\nIn-order of tree:')
    tree.inorder()

    print('\nPre-order of tree:')
    tree.preorder()

    print('\nPost-order of tree:')
    tree.postorder()
