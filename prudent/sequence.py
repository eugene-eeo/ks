from itertools import chain
from collections import Sequence as _Seq
from prudent.stream import Stream


class Sequence(Stream, _Seq):
    def __init__(self, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.cache = []

    def __iter__(self):
        return chain(self.cache, self.iload())

    def iload(self):
        for item in Stream.__iter__(self):
            self.cache.append(item)
            yield item

    def load(self, limit):
        for idx, _ in enumerate(self.iload(), 1):
            if idx >= limit:
                break

    def __getitem__(self, idx):
        size = len(self)
        if idx >= size:
            self.load(idx - (size - 1))
        return self.cache[idx]

    def __len__(self):
        return len(self.cache)
