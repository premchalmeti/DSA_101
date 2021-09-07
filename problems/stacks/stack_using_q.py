# from ds.q import Queue, exceptions
from collections import deque


class Stack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()


if __name__ == '__main__':
    s1 = Stack()
    s1.push(2)
    s1.push(1)

    # 1
    print(s1.pop())

    # 2
    print(s1.pop())
