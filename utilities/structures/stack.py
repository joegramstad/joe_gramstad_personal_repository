class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if not self.isEmpty():
            popped = self.stack[self.top]
            self.stack = self.stack[:self.top]
            self.top -= 1
            return popped

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        return self.top < 0