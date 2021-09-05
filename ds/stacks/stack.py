from ds.stacks import exceptions


class Stack:
    def __init__(self, max=None) -> None:
        self.container = []
        self.top = -1
        self.max = max

    def push(self, ele):
        if self.max and self.top == self.max-1:
            raise exceptions.StackOverFlowError(f"Stack exceeded {self.max} max size")

        self.top += 1
        self.container.append(ele)

    def pop(self):
        if self.top == -1:
            raise exceptions.StackUnderFlowError()

        self.top -= 1
        return self.container.pop()

    def peek(self) -> object:
        if self.top == -1:
            return None
        return self.container[self.top]

    def is_empty(self):
        return self.top == -1

    def clear(self):
        self.top = -1
        self.container = []

    def __len__(self):
        return len(self.container)

    def __str__(self):
        return f"{', '.join(self.container)}"

    __repr__ = __str__

    def __bool__(self):
        return self.is_empty()


if __name__ == '__main__':
    emps = Stack()

    emps.push('prem')
    emps.push('kartik')

    print(emps.pop())
    print(emps.peek())
