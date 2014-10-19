class Block(object):
    def __init__(self, iterable, size):
        self.size = size
        self.iterable = iter(iterable)
        self.loaded = []

    def __len__(self):
        return self.size

    def __iter__(self):
        for item in self.loaded:
            yield item

        size = self.size
        loaded = len(self.loaded)
        if loaded < size:
            for _ in range(size - loaded):
                value = next(self.iterable)
                self.loaded.append(value)
                yield value

    def __getitem__(self, idx):
        for index, item in enumerate(self):
            if idx == index:
                return item
        raise IndexError
