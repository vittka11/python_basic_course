class Student:
    def __init__(self, gender, age, name, surname, record_book):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname
        self.record_book = record_book

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))