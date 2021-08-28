
def rev_no(no):
    rno = 0

    while no != 0:
        rem = no % 10
        rno = rno * 10 + rem
        no /= 10

    return rno


def check_pal(no):
    sno = str(no)
    n = len(sno)

    for i in range(n):
        if sno[i] != sno[n-i-1]:
            return False

    return True


if __name__ == "__main__":
    no = 121252121
    print check_pal(no)
    print rev_no(no) == no
