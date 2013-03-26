class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0

stack = Stack()
for element in range(1, 10):
    stack.push(element)

while not stack.empty():
    print stack.pop()
