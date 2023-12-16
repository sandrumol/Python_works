class Student:
    name:str
    rollno:int
    course:str

    def set_student(self,name,rollno,course):
        # initializing instance variables
        self.name=name
        self.rollno=rollno
        self.course=course
    
    def display_student(self):
        print(self.name,self.rollno,self.course)

stud1=Student()
stud1.set_student("sandra",57,"django")
stud1.display_student()
print(stud1)