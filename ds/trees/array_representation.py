from typing import Tuple


def randomize_tree_creation():
    import random
    import string

    height = int(input("Enter height of tree: \n"))

    no_nodes = 2**height-1
    tree = [''] * (no_nodes+1)

    for i in range(no_nodes):
        tree[i+1] = random.choice(string.ascii_uppercase)

    return tree


def find_lr_node(tree, elem) -> Tuple[bool, object, object]:
    if elem not in tree:
        return False, None, None

    k = tree.index(elem)
    return True, tree[2 * k], tree[2 * k + 1]


def create_tree():
    pass


if __name__ == '__main__':
    tree = None
    choice = None

    while choice != -1:
        choice = int(
            input(
                "1. Randomize inputs\n" \
                +"2. Enter manually\n" \
                +"3. Print Tree\n" \
                +"4. Find Node childs\n" \
                +"-1. Exit\n\n=>"
            )
        )

        if choice == 1:
            tree = randomize_tree_creation()
        elif choice == 2:
            tree = create_tree()
        elif choice == 3:
            print(tree)
        elif choice == 4:
            if not tree:
                print("Tree is currently empty")
                continue

            elem = input("Enter element to find its child: ")
            found, l, r = find_lr_node(tree, elem)

            if found:
                print("Node: ", elem)
                print("Left child: ", l)
                print("Right child: ", r)
            else:
                print(elem, "not found in tree")
