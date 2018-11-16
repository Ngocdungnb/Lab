from random import *
from fune_intro import eval
def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    c = randint (0,3)
    op = choice(["+","-","*","/"])
    r = eval(x,y,o) + c
    return [x, y, op, c]

def check_answer(x, y, op, result, user_choice):
    pass
