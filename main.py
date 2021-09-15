import random
import colorgram
from turtle import Turtle
from turtle import Screen



turtle = Turtle()
turtle.speed(10000)
screen = Screen()
screen.colormode(255)
screen.screensize(500, 500)

colors = colorgram.extract("/Users/admin/PycharmProjects/turtle_project/images.jpg", 20)


def print_colored_dot(color):
    turtle.pendown()
    rgb = color.rgb
    turtle.color(rgb)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)




turtle.penup()

y = -300
x = -300

for _ in range(len(colors)):
    turtle.home()
    turtle.sety(y)
    turtle.setx(x)
    for color in colors:
        print_colored_dot(color)

    y += 30







screen.exitonclick()