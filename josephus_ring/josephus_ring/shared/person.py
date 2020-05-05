class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age

