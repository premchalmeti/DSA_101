# uses stack ds
# dfs for trees is easier as trees are connected and there are no cycles
# inorder, preorder, postorder are dfs for tree
import os, sys;
sys.path.append(os.environ.get('DSPATH', ''));

from trees import BinaryTree


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.link_left(2)
    tree.link_right(3)

    tree.goto(3)
    tree.link_left(4)
    tree.link_right(5)

    tree.inorder()
    print()
    tree.preorder()
    print()
    tree.postorder()
    print()
