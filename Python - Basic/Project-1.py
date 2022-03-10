import random

def gamewin(comp, you):   
     if comp == you:
           return nune
     elif comp == 's':
           if you == 'w':
                return false
           else you =='g':
                return true
     elif comp == 'w':
           if you == 'g':
                return false
           else you =='s':
                return true
      elif comp == 'g':
           if you == 's':
                return false
           else you =='w':
                return true

print("comp turn: snake(s) water(w) gun(g)?")
randno = random.randint(1, 3)
     if == 1:
         comp = 's'
      elif == 2:
         comp = 'w'
      elif == 3:
         comp = 'g'
         
 you = input("your turn: snake(1) water(2) gun(3)")
   a = gamewin(comp,you)

   print(f"com choice is :{comp}")
   print(f"your choice is :{you}")

   if a == nune:
         print("game is tie!")
   elif a:
         print("you win")
   else:
         print("you lose")
   








