import turtle

t = turtle.Turtle()

t.shape("turtle")
t.shapesize(3, 3) # 거북이를 3배 확대한다.

while True:
    cmd = input("명령을 입력하시오: ")
    if cmd == 'l':# 사용자가 "l"을 입력하였으면
        t.left(90) 
        t.forward(100)
    if cmd == 'r': # 사용자가 "r"을 입력하였으면
        t.right(90) 
        t.forward(100)