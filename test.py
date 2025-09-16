import turtle
from turtle import *

t = Turtle()
t.speed('fastest')

""" def square(x):
    for i in range(73):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.right(5)
square(any) """

""" def equal(x):
    for i in range(65):
        for i in range(3):
            t.forward(100)
            t.left(120)
        t.right(5)
equal(any) """
        
def right(x):
    for i in range(65):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(135)
        t.forward(142)
    t.right(15)
right(any)

turtle.done
