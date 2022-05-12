class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"salary is {self.Salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good morning, sir")    

Devam = Employee()
Devam.Salary = 100000
Devam.getSalary("thanks")   # Employee.getsalary(Devam)
Devam.greet()   # Employee.greet()