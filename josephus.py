from copy import copy
import csv
import zipfile

from typing import Iterator, List, NoReturn, Optional

class Person:
    def __init__(self, name: str = '', age: int = 0) -> None:
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age

class Reader:
    def __iter__(self) -> NoReturn:
        raise NotImplementedError

    def __next__(self) -> NoReturn:
        raise NotImplementedError

class TxtReader(Reader):
    def __init__(self, path) -> None:
        self.file = open(path)

    def __del__(self):
        if self.file:
            self.file.close()

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self) -> Person:
        row = next(self.file)
        if not row:
            raise StopIteration
        row_ = row.strip()
        item = row_.split(',')
        name = item[0]
        try:
            age = int(item[1])
        except ValueError:
            age = 0
        return Person(name, age)
    

class CSVReader(Reader):
    def __init__(self, path: str) -> None:
        self.csv_file = open(path)
        self.csv_reader = csv.reader(self.csv_file)
    
    def __del__(self) -> None:
        if self.csv_file:
            self.csv_file.close()
    
    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self) -> Person:
        item = next(self.csv_reader)
        name = item[0]
        try:
            age = int(item[1])
        except ValueError:
            age = 0
        return Person(name, age)

class TxtInZipReader(TxtReader):
    def __init__(self, path: str, target_file: str) -> None:
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        super().__init__(target_path)

class CSVInZipReader(CSVReader):
    def __init__(self, path: str, target_file :str) -> None:    
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        super().__init__(target_path)

class JosephusRing:
    def __init__(self, reader: Optional[Reader] = None) -> None:
        self.start: int = 1
        self.step: int = 1
        self.people: List[Person] = []
        if reader:
            for some_one in reader:
                self.people.append(some_one)

    def append(self, target: Person) -> None:
        self.people.append(target)

    def pop(self, index: int) -> None:
        if index >= len(self.people):
            raise IndexError
        self.people.pop(index)

    def quert_list(self) -> List[Person]:
        ret: List[Person] = []
        temp = copy(self.people)
        size = len(temp)
        if size == 0:
            return ret

        current_index = self.start - 1
        for _ in range(size):
            current_index = (current_index + self.step - 1) % len(temp)
            obj = temp.pop(current_index)
            ret.append(obj)
        return ret

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Person:
        if not self.people:
            raise StopIteration
        current_index = self.start - 1
        index = (current_index + self.step - 1) % len(self.people)
        self.start = index + 1
        obj = self.people.pop(index)
        return obj

if __name__ == '__main__':
    print('\n从txt文件读取\n')
    txt_reader = TxtReader('person.txt')
    jos = JosephusRing(txt_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)

    print('\n从csv文件读取\n')
    csv_reader = CSVReader('person.csv')
    jos = JosephusRing(csv_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)
    
    print('\n从zip文件中的txt文件读取\n')
    txt_in_zip_reader = TxtInZipReader('person.zip', 'person.txt')
    jos = JosephusRing(txt_in_zip_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)

    print('\n从zip文件中的csv文件读取\n')
    csv_in_zip_reader = CSVInZipReader('person.zip', 'person.csv')
    jos = JosephusRing(csv_in_zip_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)
