from prudent.stream import Stream


class Pipe(Stream):
    def __init__(self, func, *args, **kwargs):
        Stream.__init__(self, *args, **kwargs)
        self.func = func

    def map(self, func):
        return self.__class__(func, self)

    def __add__(self, other):
        p = self.__class__(self.func, self)
        p.extend(other)
        return p

    def __iter__(self):
        for item in Stream.__iter__(self):
            yield self.func(item)
