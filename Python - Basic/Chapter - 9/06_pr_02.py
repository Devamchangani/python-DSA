def game():
    return 64


score = game()

f = open("F:\python\Python - Basic\hiscore.txt")
hiscore = f.read()

if hiscore<score:
      with open("F:\python\Python - Basic\hiscore.txt") as f:
          f.write(str(score))  
