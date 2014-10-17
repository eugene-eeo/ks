from ks.stream import Stream


class Sequence(Stream):
    def __init__(self, *args, **kwargs):
        self.superclass = super(Sequence, self)
        self.superclass.__init__(*args, **kwargs)
        self.loaded = []

    def load(self, n):
        it = self.superclass.__iter__()
        for _ in range(n):
            try:
                self.loaded.append(next(it))
            except StopIteration:
                break

    def __len__(self):
        return len(self.loaded)

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
