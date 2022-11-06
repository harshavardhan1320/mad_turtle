import turtle
from turtle import Turtle
from turtle import Screen
from random import Random


t = Turtle()
R = Random()
turtle.colormode(255)

t.pensize(10)



def colour():

    r = R.randint(0, 255)
    g = R.randint(0, 255)
    b = R.randint(0, 255)
    clr = (r, g, b)
    return clr


def direction():
    direct = ["n", "w", "e", "s"]
    choice = R.choice(direct)
    if choice == "n":
        t.left(90)
        t.forward(20)
    elif choice == "s":
        t.right(90)
        t.forward(20)
    elif choice == "e":
        t.forward(20)
    else:
        t.backward(20)


for _ in range(200):
    t.pencolor(colour())
    t.speed(15)
    direction()


screen = Screen()
screen.exitonclick()
