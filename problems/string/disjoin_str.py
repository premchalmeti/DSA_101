
def disjoint_repl(s1, s2):
    for ch in s1:
        if ch not in s2:
            s1 = s1.replace(ch, '+')
    return s1


if __name__ == '__main__':
    s1 = "MOHIT"
    s2 = "ROHIT"
    print disjoint_repl(s1, s2)
