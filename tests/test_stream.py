from pytest import fixture
from prudent.stream import Stream


@fixture
def stream():
    return Stream([1, 2, 3])


def test_stream_iter(stream):
    assert list(stream) == [1, 2, 3]
    assert list(stream) == []


def test_stream_extend(stream):
    stream.extend([1, 2, 3])
    assert list(stream) == [1, 2, 3] * 2
    assert list(stream) == []
