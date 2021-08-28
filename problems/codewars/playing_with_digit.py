def dig_pow(n, p):
    dsum = 0

    for digit in str(n):
        dsum += int(digit) ** p
        p += 1

    return dsum // n if dsum % n == 0 else -1


if __name__ == '__main__':
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(46288, 3))