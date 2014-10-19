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

    def __getitem__(self, idx):
        for index, item in enumerate(self):
            if idx == index:
                return item
        raise IndexError

    def __iter__(self):
        for item in self.loaded:
            yield item

        for item in Stream.__iter__(self):
            self.loaded.append(item)
            yield item
