def merge(arr1, arr2):
    arr3 = list()
    c1, c2 = 0, 0
    n1, n2 = len(arr1), len(arr2)

    while c1 < n1 and c2 < n2:
        if arr1[c1] < arr2[c2]:
            arr3.append(arr1[c1])
            c1 += 1
        else:
            arr3.append(arr2[c2])
            c2 += 1

    # if `arr1` is processed, copy rest of nos from `arr2`
    if c1 == len(arr1):
        arr3.extend(arr2[c2:])

    # if `arr2` is processed, copy rest of nos from `arr1`
    if c2 == len(arr2):
        arr3.extend(arr1[c1:])

    return arr3


if __name__ == '__main__':
    arr1 = [1, 2, 6]
    arr2 = [0, 4, 5, 6, 8]
    print(merge(arr1, arr2))
