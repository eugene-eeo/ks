from collections import deque


class Stream(object):
    """
    This datastructure forms the core of other lazy
    data structures. You are recommended to subclass
    this class when making something new, e.g. a
    lazily loaded set.
    """

    def __init__(self, iterable=()):
        self.queue = deque()
        self.extend(iterable)

    def __add__(self, other):
        u = self.__class__(self)
        u.extend(other)
        return u

    def __iter__(self):
        while self.queue:
            for datum in self.queue[0]:
                yield datum
            self.queue.popleft()

    def extend(self, it):
        """
        Extends the current stream in-place.
        """
        self.queue.append(iter(it))
