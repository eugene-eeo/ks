from pytest import fixture
from ks.mapping import Mapping


@fixture
def d():
    iterable = [('a', 1), ('b', 2)]
    return Mapping(iterable)


def test_lazymap_iter(d):
    for _ in range(2):
        assert list(d) == ['a', 'b']


def test_lazymap_getitem(d):
    assert d['a'] == 1
    assert d['b'] == 2


def test_lazymap_len(d):
    assert len(d) == 0

    assert d['a'] == 1
    assert len(d) == 1

    assert d['b'] == 2
    assert len(d) == 2
