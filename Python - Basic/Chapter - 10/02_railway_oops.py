class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train Name is {self.train}")


DCApplication = RailwayForm()
DCApplication.name = input("Enter your Name : ")
DCApplication.train = input("Enter your Train Name : ")
DCApplication.printData()