#  First parents class

class grendpa:
    
    def relation(self):
        print("This is grandpa")

# Second parents class
class father(grendpa):
    
    def relation(self):
        super().relation()
        print("This is father")


# child class

class child(father):
    
    def relation3(self):
        print(f"i am")

g = grendpa()
g.relation()

f = father()
f.relation()

c = child()
c.relation() 
c.relation3()