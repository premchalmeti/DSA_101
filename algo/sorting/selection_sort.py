
from typing import List, Any


def selection_sort(nos: List[Any], N: int):
    """
    This function takes a list and sorts them in ascending order

    The selection sort algorithm sorts an array by repeatedly finding 
    the minimum element (considering ascending order) from unsorted part 
    and putting it at the beginning.

    Selection sort is better than bubble sort as it requires less 
    no of swappings and spends time in finding minimum element

    https://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/selectionSort.htm

    param:
        nos: array of chars or ints or floats

    return: None

    complexity:
        worst:  o(n*n)
        avg:    o(n*n)
        best:   o(n)
    """
    for i in range(N):
        min_idx = i

        for j in range(i+1, N):
            if nos[j] < nos[min_idx]:
                min_idx = j

        nos[i], nos[min_idx] = nos[min_idx], nos[i]


if __name__ == "__main__":
    arr = list('premkumar')
    selection_sort(arr, len(arr))
    print(arr)
