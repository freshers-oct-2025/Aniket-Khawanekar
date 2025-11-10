class Student:
    
    school_name = "ABC High School"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def avg_age(self, other):
        return (self.age + other.age) / 2        
        
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.name = name
    def set_age(self, age): 
        self.age = age
    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school_name}")


s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

s1.avg_age(s2)

print(s1.get_name())
s1.set_age(21)

print(Student.show_school())