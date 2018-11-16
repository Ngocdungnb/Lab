from random import *
from fune_intro import eval
def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    c = randint (0,3)
    op = choice(["+","-","*","/"])
    r = eval(x,y,op) + c
    return [x, y, op, r]

def check_answer(x, y, op, result, user_choice):
while True:
    if c == 0: