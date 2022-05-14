class Employee:
    company = "camal"
    salary = 100
    location = "surat"


    #  class atributr change using (__class__)

    # def changesalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changesalary(500)
print(e.salary)
print(Employee.salary)