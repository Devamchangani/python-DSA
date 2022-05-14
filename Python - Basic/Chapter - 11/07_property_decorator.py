class Employee:
    company = "relince"
    salary = int(input("Enter your salary: "))
    salarybonus = int(input("Enter your salarybonus: "))
    # totalsalary = salary + salarybonus

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalsalary)
e.totalsalary = 60000
print(e.salary)
print(e.salarybonus)