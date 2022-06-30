from collections import deque

class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        print(self.container.pop())

    def peek(self):
        print(self.container[-1])

    def is_empty(self):
        print(len(self.container) == 0)

    def size(self):
        print( len(self.container))

f = stack()
