"""
    prudent.sequence
    ~~~~~~~~~~~~~~~~
    Implements a tuple-like object on top of the
    standard stream class, for cases where the
    values needed to be accessed by index, lazily.
"""


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

    def load(self, n):
        """
        Load at most *n* elements from the internal
        iterable.

        :param n: The number of elements to load.
        """
        iterable = Stream.__iter__(self)
        for _ in range(n):
            try:
                self.loaded.append(next(iterable))
            except StopIteration:
                break

    def __getitem__(self, idx):
        size = len(self)
        if idx >= size:
            self.load((idx + 1) - size)
        return self.loaded[idx]

    def __iter__(self):
        for item in self.loaded:
            yield item

        for item in Stream.__iter__(self):
            self.loaded.append(item)
            yield item
