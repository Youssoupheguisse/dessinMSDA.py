# le demi cercle
y=float(input("entre le rayon du  demi cercle "))
import turtle
t = turtle.Pen()
turtle.down()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(y)