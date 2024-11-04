class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        return f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}'

class Student(Human):
    def __init__(self, name, surname, age, student_id):
        super().__init__(name, surname, age)
        self.student_id = student_id
    
    def display_info(self):
        return f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Student ID: {self.student_id}'

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, surname):
        student = self.find_student(surname)
        if student:
            self.students.remove(student)
            return True
        return False

    def find_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def __str__(self):
        return ''.join(student.display_info() for student in self.students)

# Примеры использования:
if __name__ == "__main__":
    student1 = Student("John", "Doe", 20, "S12345")
    student2 = Student("Jane", "Smith", 21, "S54321")
    student3 = Student("Alice", "Johnson", 22, "S67890")

    group = Group()
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    print("Group after adding students:")
    print(group)

    print("Searching for student with surname 'Smith':")
    print(group.find_student("Smith").display_info() if group.find_student("Smith") else "Not found")

    group.remove_student("Smith")
    print("Group after removing 'Smith':")
    print(group)