## creating the student class 
class student:
    def __init__(self, name, Year, speciality, age, grade):
        self.name = name 
        self.Year = Year
        self.speciality = speciality
        self.age = age 
        self.grade = grade 
        
    def passed(self):
        print("The student passed")
    def failed(self):
        print("The student failed")


