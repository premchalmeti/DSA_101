# hackerrank: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# leetcode: https://leetcode.com/problems/linked-list-cycle/submissions/
# hackerearth: detect and remove loop
# https://www.hackerearth.com/problem/algorithm/detect-and-remove-loop-in-a-linked-list-1/


from ds.linked_list import SinglyList

# by hashing
def solve1(head):
    visited = []
    tmp_node = head

    while tmp_node:
        if tmp_node in visited:
            return 1
        visited.append(tmp_node)
        tmp_node = tmp_node.link

    return 0


# floyd's cycle finding algo
def solve2(head):
    slow_p = head
    fast_p = head

    while slow_p and fast_p and fast_p.link:
        slow_p = slow_p.link
        fast_p = fast_p.link.link

        if slow_p == fast_p:
            return 1

    return 0


# detect and remove loop
def detect_and_remove(head):
    slow_p = head
    fast_p = head
    prev = None

    while slow_p and fast_p and fast_p.link:
        slow_p = slow_p.link
        prev = fast_p
        fast_p = fast_p.link.link

        if slow_p == fast_p:
            prev.link = None
            return 1

    return 0


if __name__ == '__main__':
    list = SinglyList()

    n1 = list._create_node(1)
    n3 = list._create_node(3)

    list.append_node(n1)
    list.append_data(2)
    list.append_node(n3)

    n3.link = n1

    print(detect_and_remove(list.head))
    print(solve2(list.head))
