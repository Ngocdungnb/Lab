from random import randint,choice
from fune_intro import eval
def  generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    c = randint (0,3)
    o = choice(["+","-","*","/"])
    r = eval(x,y,o) + c
    return x , y, o , r, c
a, b, op, r, c = generate_quiz()

print (a,op,b, " = ", r)
n = input("N/Y").upper()
if n == "Y":
    if c == 0:
        print ("OK")
    else:
        print("NO")
elif n == "N":
    if c == 0:
        print("NO")
    else:
        print("OK")
