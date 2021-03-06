from collections.abc import Iterable

class Person():
    def __init__(self, name: str = None, age: int = 0) -> None:
        self.name = name
        if age < 0:
            self.age = 0
        else:
            self.age = age  

    def __eq__(self, obj):
        return self.name == obj.name and self.age == obj.age