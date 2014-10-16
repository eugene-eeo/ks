from ks.queue import Queue
from pytest import fixture, raises


@fixture
def q():
    return Queue([1, 2, 3])


def test_queue_enqueue(q):
    q.enqueue(1)
    q.enqueue(2)
    assert list(q) == [1, 2, 3, 1, 2]
    assert list(q) == []


def test_queue_dequeue(q):
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

    with raises(ValueError):
        q.dequeue()
