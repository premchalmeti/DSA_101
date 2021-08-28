
def is_prime(no, i):
    if i == 2:
        return True
    return False if no % i == 0 else is_prime(no, i-1)


if __name__ == "__main__":
    no = 11
    print(is_prime(no, no-1))
