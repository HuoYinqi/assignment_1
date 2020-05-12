from collections.abc import Iterable

from josephus.domain.reader import Reader

def test_reader_is_iterable():
    reader = Reader()

    assert isinstance(reader, Iterable)