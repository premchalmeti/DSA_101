## Tree: 

- finite set of nodes connected via edge/branches in hierarchical fashion
- a non-linear DS

                M
            /   |  \   \
            B   C   R   E
         /   \        /   \
        k     G      F     L


## Terminology:

    - node: element of a tree (M, B)

    - edges/branches: the lines connecting the nodes

    - parent node: immediate predecessor of a node [M is parent of B, C, R, E]

    - Child node: immediate successor of a node [B, C, R, E are childs of M]

    - Root node: node that doesnt have a parent node [M is root]

    - terminal/leaf node: node that doesnt have child node. All other nodes are non-terminal nodes [K, G, F, L]

    - level: distance of that node from root. root node is at distance 0 [B,C,R,E is level 1, K,G,F,L is level 2]

    - height/depth of a tree: highest level of a tree + 1 [height of above tree is 3]

    - siblings: two or more nodes having same parent [B, C are siblings]

    - path: path of a node is sequence of nodes [path of k is M->B->K]

    - Ancestor and Descendent: [M, B are ancestor of k]
        - if Na node lies in the unique path from root node to Nm then Na is ancestor of Nm. 
        - Nm us descendent of Na

    - Subtree: [BKG is subtree, C is subtree, R is subtree, EFL is another subtree]
        - tree can be divided into subtrees

    - degree:
        - the no of subtrees or child nodes is degree
        - M: 4, B: 2, C: 0

    - forest:
        - if root is removed we get forest of subtrees
    

## Types of trees:

1. [General tree](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/tree.py)
    - a tree with N nodes
    - a tree node holds array of child nodes

        ![General Tree](https://media.geeksforgeeks.org/wp-content/uploads/20200219144238/General-Tree-vs-Binary-Tree.png)

2. [Binary Tree](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/binary_tree.py)

    - a tree with at most 2 childs called binary tree.
    - we name them left child and right child
    - a binary tree contains,
        - data
        - ptr to left child
        - ptr to right child

    Properties:

    - max nodes: the max no of nodes on level i is 2^i where i>=0
    - min nodes: if `h` is height of tree `h` min nodes 
    - height:
        - if tree has `n` nodes,
            max height: `n`
            min height: `log2(n+1)`
    - nodes/edges: 
        - n is no of nodes
        - e is edges then e = n-1

    ![Binary Tree](https://media.geeksforgeeks.org/wp-content/cdn-uploads/binary-tree-to-DLL.png)

    ### Types of Binary Tree:

    1. Strictly Binary Tree:
        - if each node has 0 or 2 nodes

        ![Strictly Binary Tree](https://i.stack.imgur.com/6d3po.gif)

    2. Extended Binary Tree:
        - if we replace the null link of each leaf node with a special node it becomes a extended binary tree.

        ![Extended Binary Tree](https://media.geeksforgeeks.org/wp-content/uploads/20191016000923/Extended1-1024x421.png)


    3. Full Binary Tree:
        - All levels have maximum no of nodes
        - h is height then has 2^h - 1 nodes

        - height 3 will have 7 nodes
        - height 4 will have 15 nodes

        ![Full Binary Tree](https://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/FullBinary.jpg)

    4. Complete Binary Tree:
        - all levels have max no of nodes except possibly the last level and all these nodes are towards left
        - Full binary is special case of Complete Binary Tree

        ![Complete Binary Tree](https://www.techiedelight.com/wp-content/uploads/Complete-Binary-Tree.png)


3. [Binary Search Tree](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/binary_search_tree.py)
4. B Tree
5. B+ Tree
6. Red-black Tree
7. AVL Tree
8. Heap
9. [Trie](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/trie.py)


## Representation:

1. [Array representation](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/array_representation.py)

    - index all the nodes from `1 - n`
    - for node `k` put element in `tree[k]` and if a node is missing keep entry blank
    - for node stored at `k` 
        - the left child will be at `2*k` 
        - the right will be `2*k+1`
        - its parent will be at `floor(k/2)`

    ![array representation](https://lh4.ggpht.com/-u2Lb-zvWCFE/ULBxmsa1mbI/AAAAAAAACFk/ZOAvwzAsJaU/clip_image001%25255B4%25255D_thumb%25255B1%25255D.gif?imgmax=800)


2. [Linked representation](https://github.com/premchalmeti/DS_and_algos_practice/blob/master/ds/trees/binary_tree.py)

    - defining a class with data, left and right variables
    - The left and right variable holds reference of left and right node
