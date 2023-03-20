import turtle
turtle.pensize(6)
turtle.speed(200)
turtle.bgcolor("black")
turtle.left(70)


for i in range(8):
 for colours in ["yellow","blue","white","green","red","pink","purple"]:
  turtle.color(colours)
  turtle.left(100)
  turtle.left(120)
  turtle.forward(500)
