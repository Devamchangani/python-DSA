def game():
    return 98


score = game()

with open("F:\python\Python - Basic\Chapter - 9\TEXT-File\hiscore.txt") as f:
    hiscore = f.read()

if  hiscore=='':
    with open("F:\python\Python - Basic\Chapter - 9\TEXT-File\hiscore.txt", "w") as f:
          f.write(str(score))  
elif int(hiscore)<score :
      with open("F:\python\Python - Basic\Chapter - 9\TEXT-File\hiscore.txt", "w") as f:
          f.write(str(score))  
