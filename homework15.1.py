class MaxStudentsError(Exception):
     pass
class Group:
        def __init__(self, name):
            self.name = name
            self.students = []

        def add_student(self, student):
            if len(self.students) >= 10:
                raise MaxStudentsError("The group cannot contain more than 10 students!")
            self.students.append(student)

        def __str__(self):
            return f"Group: {self.name}, Students: {len(self.students)}"

group = Group("Python")
try:
        for i in range(11):
            group.add_student(f"Student {i + 1}")
            print(f"Added Student {i + 1}")

except MaxStudentsError as e:
        print("Error:", e)