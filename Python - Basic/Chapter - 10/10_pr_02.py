class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is : {self.num **2}")  
  
    def squareroot(self):
        print(f"The value of {self.num} root is : {self.num **0.5}")  
  
    def cube(self):
        print(f"The value of {self.num} cube is : {self.num **3}")  


a = int(input("Enter the number: "))
c = Calculator(a)
c.square()
c.cube()
c.squareroot()