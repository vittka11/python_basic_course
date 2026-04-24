from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, surname):
        student = self.find_student(surname)
        if student:
            self.group.remove(student)

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student
        return None

    def __str__(self):
        result = f"Group {self.number}:\n"
        for student in self.group:
            result += str(student) + "\n"
        return result