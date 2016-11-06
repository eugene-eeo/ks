from itertools import chain
from collections import Sequence as _Seq
from .stream import Stream


class Sequence(Stream, _Seq):
    """
    An indexable, mutable sequence atop a Stream.
    """

    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.cache = []

    def iload(self):
        """
        Lazily yields elements passed either to extend or
        the constructor while storing them into an internal
        list. Yields elements which have not been loaded yet.
        """
        for item in Stream.__iter__(self):
            self.cache.append(item)
            yield item

    def load(self, n):
        """
        Loads at most *n* elements into the internal cache.
        Meant for internal use.
        """
        for count, _ in enumerate(self.iload(), 1):
            if count >= n:
                break

    def __getitem__(self, idx):
        max_idx = len(self) - 1
        if idx > max_idx:
            self.load(idx - max_idx)
        return self.cache[idx]

    def __iter__(self):
        return chain(self.cache, self.iload())

    def __len__(self):
        return len(self.cache)
