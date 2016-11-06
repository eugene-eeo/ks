from itertools import chain
from collections import Mapping as _Map
from .stream import Stream


class Mapping(Stream, _Map):
    """
    A lazily filled Mapping built on a stream.
    The iterable passed to the constructor must
    be an iterable that yields (key,value) pairs.
    """

    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.cache = {}

    def iload(self):
        """
        Lazily yields the key-value pairs while
        storing them into an internal dictionary.
        Should not care about conflicts- keys that
        are loaded later override earlier ones.
        """
        for key, value in Stream.__iter__(self):
            self.cache[key] = value
            yield key

    def __iter__(self):
        return chain(self.cache, self.iload())

    def __contains__(self, key):
        return (
            key in self.cache or
            key in self.iload()
        )

    def __getitem__(self, key):
        if key not in self:
            raise KeyError
        return self.cache[key]

    def __len__(self):
        return len(self.cache)

    def __add__(self, other):
        return NotImplemented
