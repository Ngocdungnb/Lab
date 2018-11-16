from random import randint,choice
a = randint(0,10)
b = randint(0,10)
c = randint (0,3)
r1 = a + b + c
r2 = a - b + c
r3 = a * b + c
r4 = a / b + c
op_list = ["+","-","*","/"]
op = choice(op_list)
eval(a,b,op)
# if op == "+":
#     print (a,"+",b, " = ", r1)
# elif op == "-":
#     print (a,"-",b, " = ", r2)
# elif op == "*":
#     print (a,"*",b, " = ", r3)
# elif op == "/":
#     print (a,"/",b, " = ", r4)
# else: 
#     print ("not")
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
