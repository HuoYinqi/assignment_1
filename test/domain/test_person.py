import pytest

from josephus.domain.person import Person

def test_person_init_with_parameter():
    someone = Person('Bob', 12)
    
    assert someone.name == 'Bob'
    assert someone.age == 12

def test_person_init_without_parameter():
    someone = Person()

    assert someone.name == None
    assert someone.age == 0

def test_person_the_value_of_age_less_than_zero():
    with pytest.raises(ValueError):
        someone = Person(age=-1)
