from itertools import chain
from collections import Set as _Set
from .stream import Stream


class Set(Stream, _Set):
    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.cache = set()

    def __len__(self):
        return len(self.cache)

    def iload(self):
        for item in Stream.__iter__(self):
            contained = item in self.cache
            self.cache.add(item)
            if not contained:
                yield item

    def __contains__(self, item):
        return item in self.cache or item in self.iload()

    def __iter__(self):
        return chain(self.cache, self.iload())
