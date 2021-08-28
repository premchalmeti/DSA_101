
def get_pairs(nos, target):
    if not target:
        return []

    pairs = []
    l = 0
    r = len(nos)-1

    while l<r:
        _sum = nos[l]+nos[r]
        if _sum == target:
            pairs.append((nos[l], nos[r]))
            l += 1
            r -= 1
        elif _sum > target:
            r -= 1
        else:
            l += 1

    return pairs


if __name__ == '__main__':
    nos = [1, 2, -3, 6, 5, 10]
    target = 11
    print(get_pairs(nos, target))
