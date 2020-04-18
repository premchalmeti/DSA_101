def solve(s,g):
    from math import gcd
    return -1 if gcd(g, s-g) != g else (g, s-g)


if __name__ == '__main__':
    print(solve(6, 3))
