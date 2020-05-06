import pytest

from collections.abc import Iterable

from josephus_ring.domain.josephus import JosephusRing
from josephus_ring.domain.person import Person

def test_josephus_init_without_parameter():
    jos = JosephusRing()
    
    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_init_with_parameter():
    jos = JosephusRing(start = 3, step = 4)
    
    assert jos.start == 3 
    assert jos.step == 4
    assert jos.people == []

def test_josephus_value_of_start_less_than_one():
    jos = JosephusRing(start = 0)

    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_value_of_step_less_than_one():
    jos = JosephusRing(step = 0)

    assert jos.start == 1
    assert jos.step == 1
    assert jos.people == []

def test_josephus_append():
    someone_1 = Person('Bob', 12)
    someone_2 = Person('Jack', 11)
    jos = JosephusRing()

    assert jos.people == []

    jos.append(someone_1)
    
    assert jos.people == [someone_1]

    jos.append(someone_2)

    assert jos.people == [someone_1, someone_2]

def test_josephus_pop_without_paremeter():
    jos = JosephusRing()
    someone_1 = Person('Bob', 12)
    someone_2 = Person('Jack', 11)
    someone_3 = Person('Tony', 15)
    jos.people = [someone_1, someone_2, someone_3]
    jos.pop()

    assert jos.people == [someone_1, someone_2]

def test_josephus_pop_with_paremeter():
    jos = JosephusRing()
    someone_1 = Person('Bob', 12)
    someone_2 = Person('Jack', 11)
    someone_3 = Person('Tony', 15)
    jos.people = [someone_1, someone_2, someone_3]
    jos.pop(1)

    assert jos.people == [someone_1, someone_3]

def test_josephus_query_list():
    jos = JosephusRing(1, 2)
    someone_1 = Person('Bob', 12)
    someone_2 = Person('Jack', 11)
    someone_3 = Person('Tony', 15)
    jos.people = [someone_1, someone_2, someone_3]
    result = jos.query_list()

    assert result == [someone_2, someone_1, someone_3]

def test_josephus_is_iterable():
    jos = JosephusRing()
    assert isinstance(jos, Iterable)

def test_josephus_next():
    jos = JosephusRing(1, 2)
    someone_1 = Person('Bob', 12)
    someone_2 = Person('Jack', 11)
    someone_3 = Person('Tony', 15)    
    jos.people = [someone_1, someone_2, someone_3]

    assert next(jos) == someone_2
    assert next(jos) == someone_1
    assert next(jos) == someone_3
    with pytest.raises(StopIteration):
        next(jos)

