#from turtle import *
#speed(500)
#color('cyan')
#bgcolor('black')
#b = 200
#while b >0:
#    left(b)
#    forward(b * 3)
#    b=b-1
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()