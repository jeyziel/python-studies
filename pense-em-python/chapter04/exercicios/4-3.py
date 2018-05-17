import turtle
import math

bob = turtle.Turtle()

##1 : desenhar um quadrado

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

##square(bob, 80)

##desenhar um polígono

def polygon(t, length, n):
    angle = 360 / n

    for i in range(n):
        t.fd(length)
        t.lt(angle)

##polygon(bob, 70, 7)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = int(circumference / n)
    polygon(t, n, length)

circle(bob, 20.5)

turtle.mainloop()