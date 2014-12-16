"""
    prudent.sequence
    ~~~~~~~~~~~~~~~~
    Implements a tuple-like object on top of the
    standard stream class, for cases where the
    values needed to be accessed by index, lazily.
"""


from itertools import chain
from collections import Sequence as _Seq
from prudent.stream import Stream


class Sequence(Stream, _Seq):
    """
    A sequence is a special case of a stream where
    the values can be accessed lazily, but previous
    values are preserved, similar to a tuple that it
    is a read-only structure.
    """

    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.loaded = []

    def __len__(self):
        return len(self.loaded)

    def iload(self):
        """
        Iteratively load and store elements that the
        Sequence object was instantiated with.
        """
        for item in Stream.__iter__(self):
            self.loaded.append(item)
            yield item

    def load(self, limit):
        """
        Load at most *n* elements from the internal
        iterable. It does not raise an exception if
        there isn't enough elements to consume.

        :param limit: The number of elements to load.
        """
        for idx, _ in enumerate(self.iload(), 1):
            if idx == limit:
                break

    def __getitem__(self, idx):
        size = len(self)
        if idx >= size:
            self.load(idx - (size - 1))
        return self.loaded[idx]

    def __iter__(self):
        return chain(self.loaded, self.iload())
