from typing import List


def _compute_mid(left: int, right: int) -> int:
    return left + ((right - left) // 2)


def binary_search(nos: List[int], tgt: int, left: int, right: int) -> int:
    """ 
        param:
            nos: A sorted iterable for search operation
            tgt: An element to be searched
            return:
                if found: return index of tgt element
                else: return -1

        complexity:
            best: O(1)
            worst: O(log N)
            avg: O(log N)
    """

    if right < left:
        return -1

    mid = _compute_mid(left, right)

    if nos[mid] == tgt:
        return mid
    elif nos[mid] < tgt:
        return binary_search(nos, tgt, mid + 1, right)

    return binary_search(nos, tgt, left, mid - 1)


if __name__ == "__main__":
    print(binary_search([1, 2, 3], 3, 0, 3))
