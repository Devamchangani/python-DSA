'''
  ======  The Perfect Guess. ======

    We are going to write a program that generates a random number 
    and asks the user to guess it If the player's guess is higher 
    than the actual number, the program displays Lower number please.
    Similarly if the user's guess is too low, the program "prints "higher 
    number please" When the user guesses the correct number, the program 
    displays the number of guesses the player used to arrive at the number.

    Hint: use the random module


'''

import random
randnumber = random.randint(1,100)
# print(randnumber)
userguess = 0
guesses = 0


while(userguess != randnumber):
    userguess = int(input("Enter your guess: "))
    if(userguess==randnumber):
        print("Your guess is right!")
    else:
        if(userguess>randnumber):
            print(f"Your guess is wrong! Enter a smaller number compare to {userguess}")
        else:
            print(f"Your guess is wrong! Enter a large number compare to {userguess}")
    guesses += 1

print(f" you guessed the number in {guesses} guesses")

score = guesses

with open("F:\python\Python - Basic\Basic projects\Project-2_hiscore.txt") as f:
    hiscore = f.read()

if  hiscore=='':
    with open("F:\python\Python - Basic\Basic projects\Project-2_hiscore.txt", "w") as f:
        f.write(str(score))  
elif int(hiscore)>score :
    print("You have brocken the large score")
    with open("F:\python\Python - Basic\Basic projects\Project-2_hiscore.txt", "w") as f:
        f.write(str(score))  