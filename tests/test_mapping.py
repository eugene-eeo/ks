from unittest import TestCase
from prudent.mapping import Mapping


class MappingTest(TestCase):
    def setUp(self):
        self.mapping = Mapping([(1, 2), (2, 3), (3, 4)])

    def test_iter(self):
        keys = [1, 2, 3]
        for _ in range(2):
            assert list(self.mapping) == keys

    def test_contains(self):
        assert 1 in self.mapping
        assert 1 in self.mapping

    def test_getitem(self):
        assert self.mapping[1] == 2
        assert self.mapping[3] == 4
        assert self.mapping[2] == 3

    def test_len(self):
        assert len(self.mapping) == 0
        self.mapping[3]
        assert len(self.mapping) == 3

    def test_getitem_special(self):
        class BigInt(int):
            def __hash__(self):
                return 1

        mapping = Mapping([(BigInt(4), 1)])

        assert 1 not in mapping
        assert 4 not in mapping
        assert BigInt(4) in mapping
