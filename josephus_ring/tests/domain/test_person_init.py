import pytest

from josephus_ring.domain.person import Person

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

def test_person_from_dict():
    adict = {'name': 'Bob', 'age': 12}
    someone = Person.from_dict(adict)

    assert someone.name == 'Bob'
    assert someone.age == 12

def test_person_to_dict():
    someone = Person('Bob', 12)
    result = someone.to_dict()

    assert result == {'name': 'Bob', 'age': 12}

