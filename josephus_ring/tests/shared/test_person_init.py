import pytest

from josephus_ring.shared.person import Person

def test_person_init():
    someone = Person('Bob', 12)

    assert someone.name == 'Bob'
    assert someone.age == 12

def test_person_value_of_age_less_than_zero():
    with pytest.raises(ValueError):
        someone = Person('Bob', -1)

def test_person_value_of_age_is_zero():
    someone = Person('Bob', 0)

    assert someone.name == 'Bob'
    assert someone.age == 0
    