from prudent.sequence import Sequence
from pytest import fixture, raises


@fixture
def seq():
    return Sequence([1, 2, 3])


def test_sequence_getitem(seq):
    assert seq[0] == 1
    assert seq[2] == 3


def test_sequence_len(seq):
    assert len(seq) == 0
    seq.load(3)
    assert len(seq) == 3


def test_sequence_iter(seq):
    assert list(seq) == [1, 2, 3]
    seq.extend([1, 2, 3])
    assert list(seq) == ([1, 2, 3] * 2)


def test_sequence_index(seq):
    assert seq.index(2) == 1
    assert seq.index(3) == 2
    with raises(ValueError):
        seq.index(4)
