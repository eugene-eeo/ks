"""
    ks.stream
    ~~~~~~~~~
    Implements a stream object that retains the state
    of iterations and can be used as the basis for
    lazily evaluated streams.
"""


from ks.utils import pipe


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
        self.iterables = []
        self.functions = []
        self.extend(iterable)

    def __iter__(self):
        for item in self.iterables[:]:
            for datum in item:
                yield pipe(self.functions, datum)
            self.iterables.remove(item)

    def extend(self, other):
        """
        Include another iterable into the stream,
        therefore extending the stream.

        :param other: The other iterable.
        """
        self.iterables.append(iter(other))
        return self

    __lshift__ = extend

    def use(self, function):
        """
        Register a function to be used by the stream
        for piped processing of each of the datum
        inside the stream.

        :param function: The function to add to the
            internal pipeline.
        """
        self.functions.append(function)
        return self
