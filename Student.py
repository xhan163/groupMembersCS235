class Student:
    def __init__(self, name, upi):
        self.name = name
        self.upi = upi
    def get_name(self):
        return self.name
    def __set_name__(self, name):
        self.name = name

student1 = Student("Tong", "stong109")
print(student1.get_name())