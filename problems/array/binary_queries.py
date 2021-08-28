
def _to_decimal(binary_repr):
    dec = 0

    for (i, n) in enumerate(binary_repr):
        dec += (n * 2 ** i)

    return dec


def odd_even_check(lst, start, end):
    dec_no = _to_decimal(lst[start:end])
    return 'EVEN' if dec_no % 2 == 0 else 'ODD'


def flip_the_bit(bit_pos):
    pass


if __name__ == "__main__":
    N, Q = map(int, input().split())

    lst = map(int, input().split())

    cmds = {
        0: odd_even_check,
        1: flip_the_bit
    }

    for _ in range(Q):
        cmd, *cmd_args = list(map(int, input().split()))

        if cmd not in cmds:
            raise ValueError('Command not available!')

        callback = cmds[cmd]

        callback(*cmd_args)
