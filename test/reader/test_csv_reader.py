from josephus.reader.csv_reader import CSVReader
from josephus.domain.person import Person

def test_csv_reader():
    csv_reader = CSVReader('person.csv')
    result = []
    for each in csv_reader:
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

def test_csv_reader_from_zip_file():
    csv_reader = CSVReader.from_zip('person.zip', 'person.csv')
    result = []
    for each in csv_reader:
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

