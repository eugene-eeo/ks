from unittest import TestCase
from prudent.mapping import Mapping


class MappingTest(TestCase):
    def setUp(self):
        self.mapping = Mapping([(1, 2), (2, 3), (3, 4)])

    def test_iter_preserves_keys(self):
        keys = [1, 2, 3]
        for _ in range(2):
            assert list(self.mapping) == keys

    def test_contains(self):
        assert 1 in self.mapping
        assert 1 in self.mapping
        assert 3 in self.mapping

    def test_getitem(self):
        assert self.mapping[1] == 2
        assert self.mapping[3] == 4
        assert self.mapping[2] == 3

    def test_len_returns_current_size(self):
        assert len(self.mapping) == 0
        self.mapping[3]
        assert len(self.mapping) == 3

    def test_add_is_not_supported(self):
        self.assertRaises(
            TypeError,
            lambda: self.mapping + [],
        )
