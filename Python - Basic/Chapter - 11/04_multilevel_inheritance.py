#  First parents class

class grendpa:
    
    def relation(self):
        print("This is grandpa")

# Second parents class
class father(grendpa):
    
    def relation2(self):
        print("This is father")


# child class

class child(father):
    
    def relation3(self):
        print(f"i am")

g = grendpa()
g.relation()
f = father()
f.relation()
f.relation2()
c = child()
c.relation()
c.relation2()
c.relation3()