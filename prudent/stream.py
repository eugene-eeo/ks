"""
    prudent.stream
    ~~~~~~~~~~~~~~
    Implements a stream object that retains the state
    of iterations and can be used as the basis for
    lazily evaluated streams.
"""


from collections import deque


class Stream(object):
    """
    A stream represents a series of iterables that
    can be iterated over and will retain their
    iterated state.
    """

    def __init__(self, iterable):
        """
        Create a new Stream object from a given
        iterable.

        :param iterable: An iterable.
        """
        self.queue = deque()
        self.extend(iterable)

    def __iter__(self):
        while self.queue:
            for datum in self.queue[0]:
                yield datum
            self.queue.popleft()

    def extend(self, other):
        """
        Include another iterable into the stream,
        therefore extending the stream.

        :param other: The other iterable.
        """
        self.queue.append(iter(other))
