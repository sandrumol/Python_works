class Employee:  # class
    id:int
    name:str
    department:str
    salary:int

    def set_emp(self,id,name,dept,sal):       # method
        self.id=id
        self.name=name
        self.department=dept
        self.salary=sal

    def display_emp(self):          # method
        print(self.id,self.name,self.salary,self.department)

emp1=Employee()     # object
emp1.set_emp(123,"ram","hr",50000)

emp2=Employee()     # object
emp2.set_emp(345,"vijay","qa",55000)

emp1.display_emp()
emp2.display_emp()
