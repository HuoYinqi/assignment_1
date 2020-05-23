import zipfile
from typing import List, Optional

from josephus.domain.person import Person
from josephus.domain.reader import Reader
from josephus.adapter.txt_reader import TxtReader
from josephus.adapter.csv_reader import CSVReader
from josephus.use_cases.josephus import Josephus

class Interface:
    INVALID_PATH = 'abc'
    INVALID_TARGET_FILE = 'xx'
    INVALID_START = -1
    INVALID_STEP = -1
    
    def __init__(self):
        self.start: int = 1
        self.step: int = 1
        self.reader: Optional[Reader] = None
        super().__init__()

    def create_reader(self, filepath=None, target_file=None) -> None:
        if not filepath:
            return 

        if '.txt' in filepath:
            self.reader = TxtReader(filepath)

        elif '.csv' in filepath:
            self.reader = CSVReader(filepath)

        elif '.zip' in filepath and target_file:
            self.reader_from_zip(filepath, target_file)

    def reader_from_zip(self, filepath=None, target_file=None):
        if '.txt' in target_file:
            self.reader = TxtReader.from_zip(filepath, target_file)

        elif '.csv' in target_file:
            self.reader = CSVReader.from_zip(filepath, target_file)

        else:
            raise FileNotFoundError

    def get_namelist_from_zip(self, filepath) -> list:
        if '.zip' in filepath:
            with zipfile.ZipFile(filepath) as zip_file:
                if zip_file:
                    filenames: list = zip_file.namelist()
                    return filenames
        else:
            return None
    def set_start_value(self, start: str):
        self.start = int(start)
        if self.start < 1:
            raise ValueError

    def set_step_value(self, step: str):
        self.step = int(step)
        if self.step < 1:
            raise ValueError

    def create_josephus(self):
        self.josephus = Josephus(self.reader)
        self.josephus.start = self.start
        self.josephus.step = self.step

    def get_people_info(self, people) -> str:
        if people:
            people_info = ''
            for each in people:
                name = each.name
                age = str(each.age)
                people_info = people_info + name + ', ' + age + '\n'

            return people_info

    def get_result(self) -> str:
        temp = self.josephus.query_list()
        people_info = ''
        count = 1
        size = len(temp)
        for each in temp:
            name = each.name
            age = str(each.age)
            if count < size:
                people_info = people_info + 'elimination\t\t' + name + ', ' + age + '\n'
            else:
                people_info = people_info + 'winner\t\t' + name + ', ' + age + '\n'
            count += 1

        return people_info

    def check_strat_value(self):
        if self.josephus.start > len(self.josephus):
            raise ValueError
    
    def create_people_from_text(self, text: str) -> list:
        if text:
            people = []
            text = text.strip()
            persons_info = text.split('\n')
            for item in persons_info:
                info = item.split(',')
                name = info[0]
                try:
                    age = int(info[1])
                except ValueError:
                    age = 0
                people.append(Person(name, age))
            return people