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
        self.iterables = deque()
        self.extend(iterable)

    def __iter__(self):
        for item in list(self.iterables):
            for datum in item:
                yield datum
            self.iterables.popleft()

    def extend(self, other):
        """
        Include another iterable into the stream,
        therefore extending the stream.

        :param other: The other iterable.
        """
        self.iterables.append(iter(other))
