import turtle
import time
turtle.bgcolor("white")
turtle.pensize(2)
def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "red")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.left(230)
turtle.forward(80)
turtle.write("İpek", move=False, align="center", font=("Arial", 30, "normal")) 
turtle.hideturtle()
time.sleep(10)