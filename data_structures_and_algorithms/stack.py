class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        """Add element to the end of the list"""
        self.items.append(item)

    def pop(self):
        """Return and remove the last element of the list"""
        return self.items.pop()

    def peek(self):
        """Return the first element of the list"""
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(7)
    s.push(2)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s)
