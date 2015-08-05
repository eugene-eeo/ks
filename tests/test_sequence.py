from unittest import TestCase
from prudent.sequence import Sequence


class SequenceTest(TestCase):
    def setUp(self):
        self.seq = Sequence([1, 2, 3])

    def test_getitem(self):
        assert self.seq[0] == 1
        assert self.seq[2] == 3

    def test_getitem_raises_indexerror(self):
        self.assertRaises(IndexError, lambda: self.seq[3])

    def test_len_returns_current_size(self):
        assert len(self.seq) == 0
        self.seq[2]
        assert len(self.seq) == 3

    def test_iter_preserves_elems(self):
        for _ in range(2):
            assert list(self.seq) == [1, 2, 3]
