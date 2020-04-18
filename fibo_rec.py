
def fibo(n1, n2, n):
    n3 = n1+n2

    if n3 > n:
        return

    print n3,

    fibo(n2, n3, n)


if __name__ == "__main__":
    print 0, 1,
    fibo(0, 1, 5)
