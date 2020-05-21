import zipfile

from josephus.domain.reader import Reader
from josephus.domain.person import Person

class TxtReader(Reader):
    def __init__(self, path):
        try:
            self.file = open(path)
        except FileNotFoundError:
            self.file = None
            raise FileNotFoundError

    def __del__(self):
        if self.file:
            self.file.close()

    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self.file)
        if not row:
            raise StopIteration

        row_ = row.strip()
        item = row_.split(',')
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