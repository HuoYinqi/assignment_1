class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0')
        self.age = age

    @classmethod
    def from_dict(cls, adict):
        name = adict['name']
        age = adict['age']
        return cls(name, age)

    def to_dict(self):
        return {'name': self.name, 'age': self.age}
