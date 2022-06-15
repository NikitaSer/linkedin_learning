from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        """Check if the queue is empty"""
        return not self.items

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Get and remove the first item of the queue"""
        return self.items.popleft()

    def size(self):
        """Get the size of the queue"""
        return len(self.items)

    def peek(self):
        """Get first item of the queue"""
        return self.items[0]

    def __str__(self):
        """Return the items of the queue"""
        return str(self.items)\


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q)
    q.dequeue()
