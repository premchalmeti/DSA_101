from ds.q import Queue
from ds.trees import BinaryTree


def dfs(root):
    q = Queue()
    q.enq(root)

    while q:
        n = q.deq()
        print(n.data, end=' ')

        if n.left:
            q.enq(n.left)
        if n.right:
            q.enq(n.right)
    
    print()


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.link_left(2)
    tree.link_right(3)

    tree.goto(2)
    tree.link_left(4)
    tree.link_right(5)

    print('DFS of Tree is,')
    dfs(tree.get_root())
