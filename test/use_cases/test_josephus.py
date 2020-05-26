import pytest

from unittest import mock
from collections.abc import Iterable

from josephus.use_cases.josephus import Josephus
from josephus.domain.person import Person

@pytest.fixture
def people_example():
    return [Person('Bob', 12), Person('Jack', 13), Person('Peter', 14)]
    
def test_josephus_init_with_reader(people_example):
    reader = mock.MagicMock()
    reader.__iter__.return_value = people_example
    jos = Josephus(reader)

    reader.__iter__.assert_called_with()
    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == [
        Person('Bob', 12),
        Person('Jack', 13),
        Person('Peter', 14)
    ]

def test_josephus_init_with_invalid_reader():
    reader = mock.Mock()
    with pytest.raises(TypeError):
        Josephus(reader)

def test_josephus_init_without_reader():
    jos = Josephus()

    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_append():
    someone1: Person = Person('Bob', 12)
    jos = Josephus()
    jos.append(someone1)
    
    assert jos.people == [someone1]

def test_josephus_pop(people_example):
    jos = Josephus()
    jos.people = people_example
    jos.pop(1)

    assert jos.people == [Person('Bob', 12), Person('Peter', 14)]
    
def test_josephus_query_list(people_example):
    jos = Josephus()
    jos.start = 2
    jos.step = 2
    jos.people = people_example
    result = jos.query_list()

    assert result == [Person('Peter', 14), Person('Jack', 13), Person('Bob', 12)]

def test_josephus_is_iterable():
    jos = Josephus()

    assert isinstance(jos, Iterable)

def test_josephus_output_order_by_next(people_example):
    jos = Josephus()
    jos.start = 2
    jos.step = 2
    jos.people = people_example

    assert next(jos) == Person('Peter', 14)
    assert next(jos) == Person('Jack', 13)
    assert next(jos) == Person('Bob', 12)
    with pytest.raises(StopIteration):
        next(jos)

def test_josephus_len(people_example):
    jos = Josephus()
    jos.people = people_example

    assert len(jos) == 3