from typing import List


def linear_search(nos: List[int], tgt) -> int:
    """ 
    param:
        nos: An iterable for search operation
        tgt: An element to be searched
        return:
            if found: return index of tgt element
            else: return -1

    complexity:
        best: O(1)
        worst: O(N)
        avg: O(N)
    """

    for (i, n) in enumerate(nos):
        if n == tgt:
            return i
    return -1


if __name__ == "__main__":
    nos = [1, -1, 2, 2, 3, 0, 3]
    tgt = 3
    print(linear_search(nos, tgt))
