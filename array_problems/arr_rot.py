# Write a function rotate(ar[], d, n) that rotates
# arr[] of size n by d elements.

# approach 1 aux space
def app1(arr, d, n):
    aux = arr[:d]

    i = 0

    while i < n-d:
        arr[i] = arr[i+d]
        i += 1
    arr[n-d:] = aux[:]

    return arr

# approach 2 one by one rotation
def app2(arr, d ,n):

    def left_rotate(arr, n):
        import pdb; pdb.set_trace()
        tmp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]

        arr[n-1] = tmp
        return arr

    for _ in range(d):
        arr =  left_rotate(arr, len(arr))

    return arr

# approach 3 juggling algo
def approach3(arr, d, n):
    pass

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print(app2(arr, d, len(arr)))
