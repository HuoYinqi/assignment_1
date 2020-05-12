from collections.abc import Iterable

class Person():
    def __init__(self, name: str = None, age: int = 0) -> None:
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age    

    def __eq__(self, obj):
        return self.name == obj.name and self.age == obj.age