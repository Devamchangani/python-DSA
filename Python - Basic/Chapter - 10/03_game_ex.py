class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1= Remote()
Player1 = Player()


if(remote1.isLeftpressed()):
    Player1.moveLeft()
elif(remote1.isRightpressed()):
      Player1.moveRight()
elif(remote1.isToppressed()):
      Player1.moveTop()