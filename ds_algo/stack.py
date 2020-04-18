stack = list()

def push(ele):
    stack.append(ele)


def pop():
    return stack.pop()


def peek():
    return stack[-1]


if __name__ == '__main__':
    push('prem')
    push('kartik')

    print(pop())
    print(peek())
