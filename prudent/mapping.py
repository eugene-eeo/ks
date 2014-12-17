"""
    prudent.mapping
    ~~~~~~~~~~~~~~~

    Implements a lazy read-only mapping that lazily
    loads the key and value pairs into a dictionary.
"""


from itertools import chain
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
        for k, v in Stream.__iter__(self):
            self.loaded[k] = v
            yield k, v

    def __getitem__(self, key):
        if key not in self:
            raise KeyError
        return self.loaded[key]

    def __iter__(self):
        return chain(
            self.loaded,
            (k for k, _ in self.iload()),
            )

    def __contains__(self, key):
        return (key in self.loaded or
                hash(key) in (hash(k) for k, _ in self.iload()))

    def __len__(self):
        """
        Return the current size of the mapping.
        **Not guaranteed to be deterministic.**
        """
        return len(self.loaded)
