class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def display_info(self):
        print(f"students name: {self.name}\nstudents age: {self.age}\nstudents grade: {self.grade}")
    
    def is_passing(self):
        if self.grade.upper() in ["A","B","C"]:
            print("failing")
        else:
            print("Failing")

stud1 = student("max", 8, "a")
stud2 = student("Chris", 8, "B")

stud1.display_info()
stud1.is_passing()
print()
stud2.display_info()
stud2.is_passing()