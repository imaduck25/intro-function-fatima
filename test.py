import turtle
from turtle import *

t = Turtle()
t.speed('fastest')

def square(x): 
    for i in range(60):
        for i in range(4):
            t.forward(x)
            t.left(90)
square(200)

""" 
def square(x):
    for i in range(73):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.right(5)
square(any)
 """
""" def equal(x):
    for i in range(65):
        for i in range(3):
            t.forward(100)
            t.left(120)
        t.right(5)
equal(any) """
        
""" def right(x):
    for i in range(15):
        for i in range(1):
             t.forward(100)
             t.left(90)
             t.forward(100)
             t.left(135)
             t.forward(142)
        t.right(15)
right(100) """

""" def right(x):
    for i in range(80):
        for i in range(1):
             t.forward(100)
             t.left(90)
             t.forward(100)
             t.left(135)
             t.forward(142)
        t.right(3.5)
right(100) """

""" def addSquares(iRange):
    length = 25
    for i in range(iRange):
        addSquares(length, 90)
        length += 25
addSquares(5) """
""" 
def star(x):
    for i in range(5):
        t.left(144)
        t.forward(100)
star(100)

def many_stars():
    length = 25
    for i in range(60):
        star(length)
        t.right(5)
        length = length * 2
many_stars() """

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
    t.right(5)
addSquares(5)

turtle.done
