
def find_even_index(arr):
    c = 0
    rsum = sum(arr)
    lsum = 0

    while c  < len(arr):
        rsum -= arr[c]
        if lsum == rsum:    return c
        lsum += arr[c]
        c += 1

    return -1


if __name__ == '__main__':
    print(find_even_index([1,2,3,4,3,2,1]))
    print(find_even_index([1,100,50,-51,1,1]))
    print(find_even_index([1,2,3,4,5,6]))
    print(find_even_index([20,10,30,10,10,15,35]))
    print(find_even_index([20,10,-80,10,10,15,35]))
    print(find_even_index([10,-80,10,10,15,35,20]))
    print(find_even_index(range(1,100)))
    print(find_even_index([0,0,0,0,0]))
    print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
    print(find_even_index(range(-100,-1)))

