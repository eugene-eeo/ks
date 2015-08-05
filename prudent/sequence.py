from itertools import chain
from collections import Sequence as _Seq
from prudent.stream import Stream


class Sequence(Stream, _Seq):
    """
    Implements an indexable, mutable sequence atop
    the Stream class.
    """

    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.cache = []

    def iload(self):
        """
        Lazily yields elements passed either to
        extend or the constructor while storing
        them into an internal list. Yields elements
        which have not been loaded yet.
        """
        for item in Stream.__iter__(self):
            self.cache.append(item)
            yield item

    def load(self, elems):
        """
        Loads at most *elems* elements into the
        internal cache. Meant for internal use.
        """
        for count, _ in enumerate(self.iload(), 1):
            if count == elems:
                break

    def __getitem__(self, idx):
        size = len(self)
        if idx >= size:
            self.load(idx - (size - 1))
        return self.cache[idx]

    def __iter__(self):
        return chain(self.cache, self.iload())

    def __len__(self):
        return len(self.cache)
