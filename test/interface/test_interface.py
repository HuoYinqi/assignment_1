import pytest

from josephus.adapter.txt_reader import TxtReader
from josephus.interface.interface import Interface
from josephus.domain.person import Person

def test_interface_init():
    interface = Interface()

    assert interface.start == 1
    assert interface.step == 1
    assert interface.reader == None

def test_interface_create_reader_without_parameter():
    interface = Interface()
    interface.create_reader()

    assert interface.reader == None

def test_interface_create_reader_with_wrong_parameter():
    interface = Interface()
    interface.create_reader(interface.INVALID_PATH)

    assert interface.reader == None

def test_interface_create_txtreader():
    interface = Interface()
    interface.create_reader("data/person.txt")
    result: list = []
    for each in interface.reader:
        result.append(each)

    assert result == [
        Person('Bob', 15),
        Person('Jack', 12),
        Person('Allen', 17),
        Person('Tony', 20),
        Person('Peter', 15),
        Person('Rose', 16),
        Person('Wade', 19)
    ]

def test_interface_create_csvreader():
    interface = Interface()
    interface.create_reader("data/person.csv")
    result: list = []
    for each in interface.reader:
        result.append(each)

    assert result == [
        Person('Bob', 15),
        Person('Jack', 12),
        Person('Allen', 17),
        Person('Tony', 20),
        Person('Peter', 15),
        Person('Rose', 16),
        Person('Wade', 19)
    ]    

def test_interface_create_txtreader_from_zip():
    interface = Interface()
    interface.create_reader("data/person.zip", "person.txt")
    result: list = []
    for each in interface.reader:
        result.append(each)

    assert result == [
        Person('Bob', 15),
        Person('Jack', 12),
        Person('Allen', 17),
        Person('Tony', 20),
        Person('Peter', 15),
        Person('Rose', 16),
        Person('Wade', 19)
    ]

def test_interface_create_csvreader_from_zip():
    interface = Interface()
    interface.create_reader("data/person.zip", "person.csv")
    result: list = []
    for each in interface.reader:
        result.append(each)

    assert result == [
        Person('Bob', 15),
        Person('Jack', 12),
        Person('Allen', 17),
        Person('Tony', 20),
        Person('Peter', 15),
        Person('Rose', 16),
        Person('Wade', 19)
    ]

def test_interface_create_reader_from_zip_with_invalid_target_file():
    interface = Interface()
    with pytest.raises(FileNotFoundError):
        interface.create_reader("data/person.zip", interface.INVALID_TARGET_FILE)

def test_interface_create_reader_from_zip_without_target_file():
    interface = Interface()
    interface.create_reader("data/person.zip")

    assert interface.reader == None

def test_interface_get_namelist_from_zip():
    interface = Interface()
    namelist = interface.get_namelist_from_zip("data/person.zip")
    
    assert namelist == ['person.csv', 'person.txt']

def test_interface_set_start():
    interface = Interface()
    interface.set_start_value('2')
    
    assert interface.start == 2

def test_interface_set_start_with_wrong_parameter():
    interface = Interface()
    with pytest.raises(ValueError):
        interface.set_start_value(interface.INVALID_START)

def test_interface_set_step():
    interface = Interface()
    interface.set_step_value('1')
    
    assert interface.step == 1

def test_interface_set_stet_with_wrong_parameter():
    interface = Interface()
    with pytest.raises(ValueError):
        interface.set_step_value(interface.INVALID_STEP)

def test_interface_create_josephus():
    interface = Interface()
    interface.reader = TxtReader("data/person.txt")
    interface.start = 2
    interface.step = 3
    interface.create_josephus()

    assert interface.josephus.start == 2
    assert interface.josephus.step == 3
    assert interface.josephus.people == [
        Person('Bob', 15),
        Person('Jack', 12),
        Person('Allen', 17),
        Person('Tony', 20),
        Person('Peter', 15),
        Person('Rose', 16),
        Person('Wade', 19)
    ]

def test_interface_get_people_info():
    people = [Person('Bob', 12), Person('Jack', 11)]
    interface = Interface()
    info = interface.get_people_info(people)

    assert info == 'Bob, 12\nJack, 11\n'

def test_interface_get_result():
    people = [Person('Bob', 12), Person('Jack', 11)]
    interface = Interface()
    interface.reader = people
    interface.create_josephus()
    result = interface.get_result()

    assert result == "elimination Bob, 12\nwinner\tJack, 11\n"

def test_interface_check_start_value():
    interface = Interface()
    interface.strat = 3
    interface.create_josephus()
    interface.people = [Person('Bob', 12), Person('Jack', 11)]

    with pytest.raises(ValueError):
        interface.check_strat_value()

def test_interface_create_people_from_text():
    text = "Jack, 12\nBob, 11\nTony, 14"
    interface = Interface()
    people = interface.create_people_from_text(text)

    assert people[0] == Person('Jack', 12)
    assert people[1] == Person('Bob', 11)
    assert people[2] == Person('Tony', 14)
