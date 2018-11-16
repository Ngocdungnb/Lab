from turtle import *
def draw_square(t, z):
    pencolor(z)
    for i in range(4):
        forward(t)
        left(90)
draw_square(100, 'green')
