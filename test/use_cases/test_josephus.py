import pytest

from collections.abc import Iterable

from josephus.use_cases.josephus import Josephus
from josephus.domain.person import Person

def test_josephus_init():
    jos = Josephus()

    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_append():
    someone1: Person = Person('Bob', 12)
    jos = Josephus()
    jos.append(someone1)
    
    assert jos.people == [someone1]

def test_josephus_pop():
    someone1: Person = Person('Bob', 12)
    someone2: Person = Person('Jack', 13)
    someone3: Person = Person('Peter', 14)
    jos = Josephus()
    jos.people = [someone1, someone2, someone3]
    jos.pop(1)

    assert jos.people == [someone1, someone3]
    
def test_josephus_query_list():
    someone1: Person = Person('Bob', 12)
    someone2: Person = Person('Jack', 13)
    someone3: Person = Person('Peter', 14)
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
    someone1: Person = Person('Bob', 12)
    someone2: Person = Person('Jack', 13)
    someone3: Person = Person('Peter', 14)
    jos = Josephus()
    jos.start = 2
    jos.step = 2
    jos.people = [someone1, someone2, someone3]

    assert next(jos) == someone3
    assert next(jos) == someone2
    assert next(jos) == someone1
    with pytest.raises(StopIteration):
        next(jos)
    
def test_josephus_init_with_reader():
    someone1: Person = Person('Bob', 12)
    someone2: Person = Person('Jack', 13)
    someone3: Person = Person('Peter', 14)
    persons = [someone1, someone2,someone3]
    jos = Josephus(reader=persons)

    assert jos.people == [someone1, someone2, someone3]

def test_josephus_len():
    someone1: Person = Person('Bob', 12)
    someone2: Person = Person('Jack', 13)
    someone3: Person = Person('Peter', 14)
    jos = Josephus()
    jos.people = [someone1, someone2, someone3]

    assert len(jos) == 3