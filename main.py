import random
from turtle import Turtle
from turtle import Screen

turtle = Turtle()
screen = Screen()



def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    color = (r, g, b)
    return color


for i in range(360):
    turtle.pencolor(random_color())
    turtle.speed("fastest")
    turtle.circle(100)
    turtle.right(3)

screen.exitonclick()
