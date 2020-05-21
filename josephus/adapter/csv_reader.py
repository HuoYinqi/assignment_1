import csv
import zipfile

from josephus.domain.reader import Reader
from josephus.domain.person import Person

class CSVReader(Reader):
    def __init__(self, path):
        try:
            self.csv_file = open(path)
            self.csv_reader = csv.reader(self.csv_file)
        except FileNotFoundError:
            self.csv_file = None
            raise FileNotFoundError

    def __del__(self):
        if self.csv_file:
            self.csv_file.close()

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.csv_reader)
        name = item[0]
        try:
            age = int(item[1])
            if age < 0:
                age = 0
        except ValueError:
            age = 0
        return Person(name, age)


    @classmethod
    def from_zip(cls, path: str, target_file: str):
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file, 'data')

        return cls(target_path)
