from unittest import TestCase
from prudent.pipe import Pipe


class PipeTest(TestCase):
    def setUp(self):
        self.pipe = Pipe(str, [1,2,3])

    def test_iter(self):
        assert list(self.pipe) == list('123')

    def test_add(self):
        p = self.pipe + [4, 5, 6]
        assert list(p) == list('123456')

    def test_map(self):
        assert list(self.pipe.map(int)) == [1, 2, 3]
