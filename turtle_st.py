import turtle as t

def draw_polygon(length, n):
    t.shape('turtle')
    t.color('yellow')
    t.begin_fill()
    for i in range(1, 6):
        t.left(144)
        t.forward(100)
    t.exitonclick()  # 프로그램이 마우스 클릭 후 종료

draw_polygon(100, 5)