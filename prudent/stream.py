from collections import deque


class Stream(object):
    def __init__(self, iterable=[]):
        self.queue = deque()
        self.extend(iterable)

    def __add__(self, other):
        u = Stream(self)
        u.extend(other)
        return u

    def __iter__(self):
        while self.queue:
            for datum in self.queue[0]:
                yield datum
            self.queue.popleft()

    def extend(self, it):
        self.queue.append(iter(it))
