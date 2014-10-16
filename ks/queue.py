from collections import deque


class Queue(object):
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.tail = deque()

    def enqueue(self, data):
        self.tail.append(data)

    def deque(self):
        if self.tail:
            return self.tail.popleft()
        try:
            return next(self.iterable)
        except StopIteration:
            raise ValueError

    def __iter__(self):
        for item in self.iterable:
            yield item
        while self.tail:
            yield self.tail.popleft()
