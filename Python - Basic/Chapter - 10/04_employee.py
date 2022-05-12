class Employee:
    company = "google"
    salary = 50000


Devam = Employee()
Sujal = Employee()

# Creating instance attribute salary for both the object
Devam.salary = 90000
Sujal.salary = 85000

print(Devam.company)
print(Sujal.company)


# Change Company Name
Employee.company = "YouTube"

print(Devam.company)
print(Sujal.company)
print(Devam.salary)
print(Sujal.salary)

# Below line throws an error as adress is not present in instance/class
# print(Devam.address)