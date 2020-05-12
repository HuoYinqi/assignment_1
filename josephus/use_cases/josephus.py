from typing import List

from josephus.domain.reader import Reader
from josephus.domain.person import Person

class Josephus:
    def __init__(self, reader: Reader = None):
        self.start: int = 1
        self.step: int = 1
        self.people: List[Person] = []
        if reader:
            for each in reader:
                self.people.append(each)

    def append(self, target: Person) -> None:
        self.people.append(target)

    def pop(self, index: int) -> None:
        self.people.pop(index)

    def query_list(self) -> List[Person]:
        ret: List[Person] = []
        temp = self.people[:]
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

    def __next__(self) -> Person:
        if not self.people:
            raise StopIteration
        current_index = self.start - 1
        index = (current_index + self.step - 1) % len(self.people)
        self.start = index + 1
        obj = self.people.pop(index)
        return obj
