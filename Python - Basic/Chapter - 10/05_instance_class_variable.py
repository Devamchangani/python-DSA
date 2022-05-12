class Employee:
    company = "Google"
    salary = 100000

Devam = Employee()
Sujal = Employee()

# Creating instance attribute salary for both the object
Devam.salary = 90000

print(Devam.salary)
print(Sujal.salary)

# Below line throws an error as adress is not present in instance/class
# print(Devam.address)