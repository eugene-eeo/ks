"""
    ks.sequence
    ~~~~~~~~~~~
    Implements a tuple-like object on top of the
    standard stream class, for cases where the
    values needed to be accessed by index, lazily.
"""


from ks.stream import Stream


class Sequence(Stream):
    """
    A sequence is a special case of a stream where
    the values can be accessed lazily, but previous
    values are preserved, similar to a tuple that it
    is a read-only structure.
    """

    def __init__(self, *args, **kwargs):
        self.superclass = super(Sequence, self)
        self.superclass.__init__(*args, **kwargs)
        self.loaded = []

    def load(self, n):
        """
        Load at most *n* elements from a stream into
        the internal cache.

        :param n: The number of elements to load.
        """
        it = self.superclass.__iter__()
        for _ in range(n):
            try:
                self.loaded.append(next(it))
            except StopIteration:
                break

    def __len__(self):
        return len(self.loaded)

    count = len

    def __getitem__(self, idx):
        size = len(self)
        if idx >= size:
            self.load((idx + 1) - size)
        return self.loaded[idx]

    def __iter__(self):
        for item in self.loaded:
            yield item

        for item in self.superclass.__iter__():
            self.loaded.append(item)
            yield item

    def index(self, elem):
        for index, item in enumerate(self):
            if item == elem:
                return index
        raise ValueError
