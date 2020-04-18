def give_sum_series(a, b):
    if a == b: return a
    n = a if a>b else b
    a = a if a<b else b
    d = 1
    return (n//2*(2*a+(n-1)*d))


if __name__ == '__main__':
    print(give_sum_series(1, 0))
