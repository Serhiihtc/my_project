class TooManyStudentsException(Exception):
    def __init__(self, message="У групі не може бути більше 10-ти студентів"):
        self.message = message
        super().__init__(self.message)


class Student:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsException()
        self.students.append(student)

    def __str__(self):
        return ', '.join(student.name for student in self.students)


try:
    group = Group()
    for i in range(11):
        student = Student(f"Студент {i+1}")
        group.add_student(student)
except TooManyStudentsException as e:
    print(e)