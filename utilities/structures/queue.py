class Queue:
    def __init__(self):
        self.queue = []
    
    def remove(self):
        popped = None
        if not self.isEmpty():
            popped = self.queue[0]
            self.queue = self.queue[1:]
        return popped

    def add(self, data):
        self.queue.append(data)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) < 1