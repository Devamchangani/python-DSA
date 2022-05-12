class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print("**********")
        print(f"The name of the train is {self.name}")
        print(f"The seats of the available in the train are {self.seats}")
        print(f"The price of the ticket is: Rs.{self.fare}")
     
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is{self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! kindly try in tatkal")
     

intercity = Train("Intercity Express: 14963", 90, 300)
intercity.getstatus()
intercity.bookticket()
intercity.getstatus()
intercity.bookticket()
intercity.getstatus()
intercity.bookticket()
intercity.getstatus()
intercity.bookticket()