# Losange
import turtle
n = int(input("donner la longueur des cotes"))
a = int(input('donner la mesure du premier angle'))
b = (360-2*a)/2
turtle.forward(n)
turtle.left(a)
turtle.forward(n)
turtle.left(b)
turtle.forward(n)
turtle.left(a)
turtle.forward(n)
turtle.left(b)