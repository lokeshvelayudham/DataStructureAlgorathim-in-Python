class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_student_details(self):
        print(self.name, end= " ")
        print(self.age)


s = Student("lokesh",25)
s.print_student_details()
