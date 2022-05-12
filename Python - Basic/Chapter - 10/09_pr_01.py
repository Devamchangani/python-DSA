class programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f"The name is programmer is {self.name} and the product is {self.product}")

Devam = programmer("Devam", "skype")
Sujal = programmer("Sujal", "Github")
Devam.getinfo()
Sujal.getinfo()