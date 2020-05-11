class Person():
    def __init__(self, name: str = None, age: int = 0) -> None:
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age    
