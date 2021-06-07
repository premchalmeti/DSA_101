class StackUnderFlowError(Exception):
    pass


class StackOverFlowError(Exception):
    def __init__(self, max, *args: object) -> None:
        self.max = max
        super().__init__(*args)


class Stack:
    def __init__(self, max=None) -> None:
        self.max = max
        self.container = []
        self.top = -1
    
    def peek(self) -> object:
        if self.top >= 0:
            return self.container[self.top]

    def pop(self) -> object:
        if self.top == -1:
            raise StackUnderFlowError()
        self.top -= 1
        return self.container.pop()

    def push(self, elem):
        if self.top+1 == self.max:
            raise StackOverFlowError(self.max) 
        self.container.append(elem)
        self.top += 1

    def size(self) -> int:
        return self.top + 1
    
    def empty(self):
        self.container = []
        self.top = -1
