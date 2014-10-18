"""
    ks.mapping
    ~~~~~~~~~~
    Implements a lazy read-only mapping that lazily
    loads the key and value pairs into a dictionary.
"""


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

    def __getitem__(self, key):
        if key in self.cache:
            return self.cache[key]
        for k, v in self.iterable:
            self.cache[k] = v
            if key == k:
                return v
        raise KeyError

    def __iter__(self):
        for item in self.cache:
            yield item
        for k, v in self.iterable:
            self.cache[k] = v
            yield k

    def __len__(self):
        """
        Return the current size of the mapping.
        **Not guaranteed to be deterministic.**
        """
        return len(self.cache)
