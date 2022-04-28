import random

# snake water gun or rock paper scissors 

def gamewin(comp, you):   
# if two values are equal, declare a tie! 
     if comp == you:
          return None

     # check for all possibilities when computer chose s 
     
     elif comp == 's':
          if you == 'w':
               return False
          elif you =='g':
                return True
     
     # check for all possibilities when computer chose w
     
     elif comp == 'w':
          if you == 'g':
                return False
          elif you =='s':
                return True

     # check for all possibilities when computer chose g

     elif comp == 'g':
          if you == 's':
                return False
          elif you =='w':
                return True

print("comp turn: snake(s) water(w) gun(g)?")

randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
           
you = input("your turn: snake(s) water(w) gun(g): ")
a = gamewin(comp, you)

print(f"com choice is :{comp}")
print(f"your choice is :{you}")

if a == None:
    print("game is tie!")
elif a:
    print("you win")
else:
    print("you lose")
   








