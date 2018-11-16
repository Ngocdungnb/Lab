from turtle import *
def draw_star(x,y,z):
    penup()
    goto(x, y)
    pendown()
    left(36)
    for i in range(5):
        forward(z)
        left(144)
draw_star(40, 100, 200)