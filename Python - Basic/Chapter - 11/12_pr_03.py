class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return self.salary * self.increment 

    @salaryafterincrement.setter
    def salaryafterincrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryafterincrement)
print(e.increment)

e.salaryafterincrement = 8000
print(e.increment)
