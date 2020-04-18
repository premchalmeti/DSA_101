
def find_pair_with_given_sum(arr, n, sum):
    l = 0
    r = n-1

    # pair = []

    while l < r:
        if arr[l] + arr[r] == sum:
            # pair.append((arr[l], arr[r]))
            return (arr[l], arr[r])
        elif arr[l] + arr[r] > sum:
            r -= 1
        else:
            l += 1

if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8]
    arr.sort()
    print find_pair_with_given_sum(arr, len(arr), 16)
