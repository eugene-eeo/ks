from unittest import TestCase
from prudent.stream import Stream


class StreamTest(TestCase):
    def setUp(self):
        self.stream = Stream([1, 2, 3])

    def test_extend(self):
        self.stream.extend([4, 5])
        self.stream.extend([6])
        assert list(self.stream) == [1, 2, 3, 4, 5, 6]

    def test_iter(self):
        assert list(self.stream) == [1, 2, 3]
        assert list(self.stream) == []

    def test_add(self):
        u = self.stream + [1]
        assert list(u) == [1, 2, 3, 1]
