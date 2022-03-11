import turtle
turtle.pensize(3)
turtle.speed(2)
turtle.bgcolor("black")

for i in range(8):
 for colours in ["yellow","blue","white","green","red","pink","purple"]:
  turtle.color(colours)
  turtle.left(100)
  turtle.left(60)
  turtle.forward(500)
