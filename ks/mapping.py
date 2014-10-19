"""
    ks.mapping
    ~~~~~~~~~~
    Implements a lazy read-only mapping that lazily
    loads the key and value pairs into a dictionary.
"""


from itertools import chain
from collections import Mapping as _Map


class Mapping(_Map):
    """
    A Mapping represents a read-only mapping that
    can lazily load the key-value pairs only when
    they are required. It is a subclass of
    ``collections.Mapping``.
    """

    def __init__(self, iterable):
        """
        Initialise a mapping instance from a given
        iterable. Note that the iterable will only
        be iterated once.

        :param iterable: The iterable.
        """
        self.iterable = iter(iterable)
        self.cache = {}

    def iload(self):
        """
        Iteratively load the key-value pairs of the
        iterable the mapping was instantiated with.
        """
        for k, v in self.iterable:
            self.cache[k] = v
            yield k, v

    def extend(self, other):
        """
        Extends the iterable of the mapping. With a
        given iterable *other*.

        :param other: The other iterable.
        """
        self.iterable = chain(self.iterable, iter(other))

    def __getitem__(self, key):
        if key in self.cache:
            return self.cache[key]
        for k, v in self.iload():
            if key == k:
                return v
        raise KeyError

    def __iter__(self):
        for k in self.cache:
            yield k
        for k, v in self.iload():
            yield k

    def __contains__(self, key):
        return (key in self.cache or
                key in (k[0] for k in self.iload()))

    def __len__(self):
        """
        Return the current size of the mapping.
        **Not guaranteed to be deterministic.**
        """
        return len(self.cache)
