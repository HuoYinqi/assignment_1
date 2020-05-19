from josephus.reader.txt_reader import TxtReader
from josephus.domain.person import Person

def test_txt_reader():
    txt_reader = TxtReader("data/person.txt")
    result = []
    for each in txt_reader:
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

def test_txt_reader_from_zip_file():
    txt_reader = TxtReader.from_zip('data/person.zip', 'person.txt')
    result = []
    for each in txt_reader:
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