from ks.queue import Queue
from pytest import fixture, raises


@fixture
def q():
    return Queue([1, 2, 3])


def test_queue_push(q):
    q.push(1)
    q.push(2)
    assert list(q) == [1, 2, 3, 1, 2]
    assert list(q) == []


def test_queue_pop(q):
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3

    with raises(ValueError):
        q.pop()
