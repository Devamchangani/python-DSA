class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(f"Employee is created")

    def getdetails(self):
        print(f"The name employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"salary is {self.Salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good morning, sir") 

Devam = Employee("Devam", 500, "Youturb")  
# Devam = Employee() --> This throws an error (missing 3 required positional arguments:)
Devam.getdetails()      