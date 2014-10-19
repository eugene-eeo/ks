from pytest import fixture
from prudent.mapping import Mapping


@fixture
def d():
    iterable = [('a', 1), ('b', 2)]
    return Mapping(iterable)


def test_mapping_iter(d):
    for _ in range(2):
        assert set(d) == set('ab')


def test_mapping_getitem(d):
    assert d['a'] == 1
    assert d['b'] == 2


def test_mapping_len(d):
    assert len(d) == 0

    assert d['a'] == 1
    assert len(d) == 1

    assert d['b'] == 2
    assert len(d) == 2


def test_mapping_extend(d):
    d.extend([('c', 3)])
    assert d['c'] == 3
