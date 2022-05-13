#  parant class

class Employee:
    company = "Google"

    def showdetails(self):
        print("This is employee")


# child class

class programmer(Employee):
    language = "python"
    # company = "youturb"

    def getlanguage(self):
        print(f"the language is {self.language}")

    # def showdetails(self):
    #     print("This is programmer")

e = Employee()
e.showdetails()
p = programmer()
p.getlanguage()
p.showdetails()
print(p.company)
print(e.company)