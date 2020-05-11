import pytest

from collections.abc import Iterable

from josephus.domain.josephus import Josephus
from josephus.share.person import Person

someone1: Person = Person('Bob', 12)
someone2: Person = Person('Jack', 13)
someone3: Person = Person('Peter', 14)

def test_josephus_init():
    jos = Josephus()

    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_append():
    jos = Josephus()
    jos.append(someone1)
    
    assert jos.people == [someone1]

def test_josephus_pop():
    jos = Josephus()
    jos.people = [someone1, someone2, someone3]
    jos.pop(1)

    assert jos.people == [someone1, someone3]
    
def test_josephus_query_list():
    jos = Josephus()
    jos.start = 2
    jos.step = 2
    jos.people = [someone1, someone2, someone3]
    result = jos.query_list()

    assert result == [someone3, someone2, someone1]

def test_josephus_is_iterable():
    jos = Josephus()

    assert isinstance(jos, Iterable)

def test_josephus_output_order_by_next():
    jos = Josephus()
    jos.start = 2
    jos.step = 2
    jos.people = [someone1, someone2, someone3]

    assert next(jos) == someone3
    assert next(jos) == someone2
    assert next(jos) == someone1
    with pytest.raises(StopIteration):
        next(jos)
    