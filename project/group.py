from student import Student

class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()
    
    def add_student(self, student: Student):
        self.students.add(student)
    
    def delete_student(self, last_name):
        self.students = {student for student in self.students if student.last_name != last_name}
    
    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None
    
    def __str__(self):
        return f'Group {self.name}:' + ''.join([str(student) for student in self.students])