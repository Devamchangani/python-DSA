#  First parents class

class mother:
    
    def relation(self):
        print("This is mother")

# Second parents class
class father:
    
    def relation2(self):
        print("This is father")


# child class

class child(mother, father):
    
    def relation3(self):
        print(f"i am")

m = mother()
m.relation()
f = father()
f.relation2()
c = child()
c.relation3()
c.relation2()
c.relation()