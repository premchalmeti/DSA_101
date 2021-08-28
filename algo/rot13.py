import string


def encrypt(msg, k):
    return "".join([string.ascii_lowercase[(string.ascii_lowercase.index(c)+k)%26] for c in msg])


def decrypt(msg, k):
    return "".join([string.ascii_lowercase[(string.ascii_lowercase.index(c)-k)%26] for c in msg])


if __name__ == '__main__':
    msg = "abcdef"
    k = 30

    e_msg = encrypt(msg, k)

    print(e_msg)

    print(decrypt(e_msg, k))

