from typing import List, Any


def bubble_sort(nos: List[Any]):
    """
    This function takes a list and sorts them in ascending order

    Bubble Sort is the simplest sorting algorithm that works by repeatedly 
    swapping the adjacent elements if they are in wrong order.

    param:
        nos: array of chars or ints or floats

    return: None

    complexity:
        worst:  o(n*n)
        avg:    o(n*n)
        best:   o(n)
    """
    N = len(nos)

    for ps in range(N):
        swapped = False

        for j in range(N - ps - 1):
            if nos[j] > nos[j+1]:
                nos[j], nos[j + 1] = nos[j + 1], nos[j]
                swapped = True

        if not swapped:
            break


def bubble_sort_rec(nos: List[Any], N):
    if N == 1:
        return

    swapped = False

    for i in range(N - 1):
    
        if nos[i] > nos[i + 1]:
            nos[i], nos[i + 1] = nos[i + 1], nos[i]
            swapped = True

    if not swapped:
        return

    bubble_sort_rec(nos, N - 1)


if __name__ == "__main__":
    arr = list('premkumar')
    bubble_sort_rec(arr, len(arr))
    print(arr)
