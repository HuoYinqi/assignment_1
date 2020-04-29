from copy import copy
import csv
import zipfile

class Person:
    def __init__(self, name = '', age = 0):
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age

class Reader:
    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

class TxtReader(Reader):
    def __init__(self, path):
        self.file = open(path)

    def __iter__(self):
        return self
    
    def __next__(self):
        row = self.file.readline()
        if not row:
            self.file.close()
            raise StopIteration
        row_ = row.strip()
        item = row_.split(',')
        name = item[0]
        age = int(item[1])
        return Person(name, age)

class CSVReader(Reader):
    def __init__(self, path):
        self.csv_file = open(path)
        csv_reader = csv.reader(self.csv_file)
        self.it =  csv_reader.__iter__()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.it.__next__()
        except StopIteration:
            self.csv_file.close()
            raise StopIteration
        name = item[0]
        age = int(item[1])
        return Person(name, age)

class TxtInZipReader(TxtReader):
    def __init__(self, path, target_file):
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        TxtReader.__init__(self, target_path)

class CSVInZipReader(CSVReader):
    def __init__(self, path, target_file):    
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        CSVReader.__init__(self, target_path)

class JosephusRing:
    def __init__(self, reader = None):
        self.start = 1
        self.step = 1
        self.people = []
        if reader:
            for some_one in reader:
                self.people.append(some_one)

    def append(self, target):
        self.people.append(target)

    def pop(self, index):
        if index >= len(self.people):
            raise IndexError
        self.people.pop(index)

    def quert_list(self):
        ret = []
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

    def __iter__(self):
        return self

    def __next__(self):
        if not self.people:
            raise StopIteration
        current_index = self.start - 1
        index = (current_index + self.step - 1) % len(self.people)
        self.start = index + 1
        obj = self.people.pop(index)
        return obj

if __name__ == '__main__':
    print('\n从txt文件读取\n')
    txt_reader = TxtReader('D:\\软件培训\\库\\person.txt')
    jos = JosephusRing(txt_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)

    print('\n从csv文件读取\n')
    csv_reader = CSVReader('D:\\软件培训\\库\\person.csv')
    jos = JosephusRing(csv_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)
    
    print('\n从zip文件中的txt文件读取\n')
    txt_in_zip_reader = TxtInZipReader('D:\\软件培训\\库\\person.zip', 'person.txt')
    jos = JosephusRing(txt_in_zip_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)

    print('\n从zip文件中的csv文件读取\n')
    csv_in_zip_reader = CSVInZipReader('D:\\软件培训\\库\\person.zip', 'person.csv')
    jos = JosephusRing(csv_in_zip_reader)
    jos.start = 3
    jos.step = 4
    for each in jos.people:
        print(each.name, each.age)
    print('--------------')
    for each in jos:
        print(each.name, each.age)
