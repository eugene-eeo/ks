"""
    prudent.mapping
    ~~~~~~~~~~~~~~~
    Implements a lazy read-only mapping that lazily
    loads the key and value pairs into a dictionary.
"""


from collections import Mapping as _Map
from prudent.stream import Stream


class Mapping(Stream, _Map):
    """
    A Mapping represents a read-only mapping that
    can lazily load the key-value pairs only when
    they are required. It is a subclass of
    ``collections.Mapping`` and ``Stream``.
    """

    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.loaded = {}

    def iload(self):
        """
        Iteratively load the key-value pairs of the
        iterable the mapping was instantiated with.
        """
        for k, value in Stream.__iter__(self):
            self.loaded[k] = value
            yield k, value

    def __getitem__(self, key):
        if key in self.loaded:
            return self.loaded[key]
        for k, value in self.iload():
            if key == k:
                return value
        raise KeyError

    def __iter__(self):
        for k in self.loaded:
            yield k
        for k, _ in self.iload():
            yield k

    def __contains__(self, key):
        return (key in self.loaded or
                key in (k[0] for k in self.iload()))

    def __len__(self):
        """
        Return the current size of the mapping.
        **Not guaranteed to be deterministic.**
        """
        return len(self.loaded)
