class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"Students enrolled in {self.course_name}:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")

student1 = Student("Nimal", "S001")
student2 = Student("Kamal", "S002")
student3 = Student("Sunil", "S003")

course = Course("Programming Fundamentals")
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

course.list_students()
