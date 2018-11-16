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
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    z = random.randint(3, 10)
    draw_star(x, y, z)
